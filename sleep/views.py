from datetime import date, datetime, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from sleep.models import Sleep
from sleep.forms import SleepForm

# Create your views here.
class SleepListView(ListView):
    model = Sleep
    paginate_by = 100
    template_name = 'sleep/sleep_list.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Sleep.objects.filter(user=user).order_by('-date')

class SleepDetailView(DetailView):
    model = Sleep
    template_name = 'sleep/sleep_detail.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Sleep.objects.filter(user=user)

class SleepCreateView(CreateView):
    model = Sleep
    form_class = SleepForm
    template_name = 'sleep/sleep_form.html'
    

    # print(date_list)
    # extra_context = {'date_list': date_list}
    
    def form_valid(self, form):
        date_list = [sleep_date['date'] for sleep_date in Sleep.objects.filter(user=self.request.user).values('date')]
        print(date_list)

        date = form.cleaned_data.get('date')
        if date in date_list:
            return HttpResponseRedirect(self.get_error_url())

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())   

    # def form_invalid(self, form):
    #     date_list = [sleep_date['date'] for sleep_date in Sleep.objects.values('date')]
    #     print(date_list)

    #     date = form.cleaned_data.get('date')
    #     if date in date_list:
    #         return HttpResponse("form is invalid.. this is just an HttpResponse object")


    def get_success_url(self):
        messages.success(self.request, 'Sen został dodany!')
        return reverse_lazy('sleep:sleep_list')

    def get_error_url(self):
        messages.error(self.request, 'Sen w tym dniu już jest dodany! Możesz zaaktualizować w każdej chwili.')
        return reverse_lazy('sleep:sleep_list')

class SleepUpdateView(UpdateView):
    model = Sleep
    form_class = SleepForm
    template_name = 'sleep/sleep_form.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Sleep.objects.filter(user=user)
    
    def get_success_url(self):
        messages.success(self.request, 'Sen został zaaktualizowany!')
        return reverse('sleep:sleep_detail', kwargs={'pk': self.object.pk})

class SleepDeleteView(DeleteView):
    model = Sleep
    template_name = 'sleep/sleep_confirm_delete.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Sleep.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Sen został usunięty!')
        return reverse_lazy('sleep:sleep_list')

def SleepChartView(request):
    all_sleep = Sleep.objects.filter(user=request.user).order_by('date')

    date_list = [sleep_date['date'] for sleep_date in Sleep.objects.filter(user=request.user).order_by('date').values('date').distinct()]

    today = datetime.now()    
    print(today.date())
    n_days_ago = today - timedelta(days=14)

    date_last14 = []

    for i in range(14, -1 ,-1):
        n_days_ago = today - timedelta(days=i)
        date_last14.append(n_days_ago.date())

    sum_value_at_date = []
    

    for sleep_date in date_last14:
        activities_tot = Sleep.objects.filter(user=request.user).aggregate(s=Sum('duration_time', filter=Q(date=sleep_date)))['s']
        if activities_tot is None:
            sum_value_at_date.append(0)
        else:
            sum_value_at_date.append(activities_tot)

    sum = 0
    items = 0
    for item in sum_value_at_date:
        if item != 0:
            sum += item
            items += 1

    if items == 0:
        average = 0
    else:
        average = sum/items
    print(average)

    print(sum_value_at_date)

    first_date_of_14_days = date_last14[0]
    last_date_of_14_days = date_last14[-1]

    context = {
        'all_sleep': all_sleep,
        'date_last14': date_last14,
        'data': sum_value_at_date,
        'first_date_of_14_days': first_date_of_14_days,
        'last_date_of_14_days': last_date_of_14_days,
        'sleep_avg': average
    }

    return render(request, 'sleep/sleep_chart.html', context=context)


