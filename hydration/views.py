from calendar import weekday
from datetime import date, datetime, timedelta
from urllib import request
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from hydration.forms import WaterForm
from hydration.models import Water

# Income View
class WaterListView(ListView):
    model = Water
    paginate_by = 100
    template_name = 'hydration/hydration_list.html'
    extra_context = {'list_what': 'water', 'today': date.today().strftime("%d/%m/%Y")}

    def get_queryset(self):
        user = self.request.user
        return Water.objects.filter(user=user, date=date.today()).order_by('-created_at_time')

    

class WaterDetailView(DetailView):
    model = Water
    template_name = 'hydration/hydration_detail.html'
    extra_context = {'detail_what': 'water'}

    def get_queryset(self):
        user = self.request.user
        return Water.objects.filter(user=user)

class WaterCreateView(CreateView):
    model = Water
    form_class = WaterForm
    template_name = 'hydration/hydration_form.html'
    extra_context = {'header': 'Dodaj napój'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        Water.objects.filter(value=1).update(real_value=100)
        Water.objects.filter(value=2).update(real_value=200)
        Water.objects.filter(value=3).update(real_value=400)
        Water.objects.filter(value=4).update(real_value=500)
        Water.objects.filter(value=5).update(real_value=1000)
        messages.success(self.request, 'Napój został dodany!')
        return reverse_lazy('hydration:water_list')

class WaterUpdateView(UpdateView):
    model = Water
    form_class = WaterForm
    template_name = 'hydration/hydration_form.html'
    extra_context = {'header': 'Update water'}

    def get_queryset(self):
        user = self.request.user
        return Water.objects.filter(user=user)
    
    def get_success_url(self):
        messages.success(self.request, 'Napój został zaaktualizowany!')
        return reverse('hydration:water_detail', kwargs={'pk': self.object.pk})

class WaterDeleteView(DeleteView):
    model = Water
    template_name = 'hydration/hydration_confirm_delete.html'
    extra_context = {'delete_what': 'Water'}

    def get_queryset(self):
        user = self.request.user
        return Water.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Napój został usunięty!')
        return reverse_lazy('hydration:water_list')

def WaterChartView(request):
    all_water_today = Water.objects.filter(date=date.today(), user=request.user)

    date_list = [water_date['date'] for water_date in Water.objects.filter(user=request.user).values('date').distinct()]

    sum_value_at_date = []
    for water_date in date_list:
        wate_tot = Water.objects.filter(user=request.user).aggregate(s=Sum('real_value', filter=Q(date=water_date)))['s']
        sum_value_at_date.append(wate_tot)

    context = {
        'all_water_today': all_water_today,
        'date': date_list,
        'data': sum_value_at_date
    }

    return render(request, 'hydration/hydration_chart.html', context=context)


def WaterHistoryView(request):
    # all_water = Water.objects.all()

    # date_list = [water_date['date'] for water_date in Water.objects.values('date').distinct()]

    # today = datetime.now()
    # n_days_ago = today - timedelta(days=14)

    # date_last14 = []

    # for i in range(14, -1 ,-1):
    #     n_days_ago = today - timedelta(days=i)
    #     date_last14.append(n_days_ago.date())
        

    # date_list_view = []
    # sum_value_at_date = []
    # for water_date in date_last14:
    #     wate_tot = Water.objects.aggregate(s=Sum('real_value', filter=Q(date=water_date)))['s']
    #     date_list_view.append(water_date)
    #     sum_value_at_date.append(wate_tot)

    # N = 14
    # date_list_view_last_14_days = date_list_view[-N:]
    # first_date_of_14_days = date_list_view_last_14_days[0]
    # last_date_of_14_days = date_list_view_last_14_days[-1]

    # context = {
    #     'all_water': all_water,
    #     'date_list_view': date_list_view,
    #     'date_list_view_last_14_days': date_list_view_last_14_days,
    #     'first_date_of_14_days': first_date_of_14_days,
    #     'last_date_of_14_days': last_date_of_14_days,
    #     'date': date_list,
    #     'data': sum_value_at_date
    # }

    all_water_today = Water.objects.filter(date=date.today(), user=request.user)

    all_water = Water.objects.filter(user=request.user).order_by('date')

    # type_list = [activity_type['type'] for activity_type in Water.objects.filter(user=request.user).values('type')]

    # print(type_list)

    date_list = [activity_date['date'] for activity_date in Water.objects.filter(user=request.user).values('date').distinct()]

    today = datetime.now()
    n_days_ago = today - timedelta(days=14)

    date_last14 = []

    for i in range(14, -1 ,-1):
        n_days_ago = today - timedelta(days=i)
        date_last14.append(n_days_ago.date())

    #print("Daty",date_last14)

    sum_value_at_date = []
    activity_label = []

    # for activity in all_water_today:
    #     activity_label.append(activity.type)

    for activity_date in date_last14:
        activities_tot = Water.objects.filter(user=request.user).aggregate(s=Sum('real_value', filter=Q(date=activity_date)))['s']
        if activities_tot is None:
            sum_value_at_date.append(0)
        else:
            sum_value_at_date.append(activities_tot)

    print(sum_value_at_date)

    first_date_of_14_days = date_last14[0]
    last_date_of_14_days = date_last14[-1]

    context = {
        'all_activities_today': all_water_today,
        'all_activities': all_water,
        'first_date_of_14_days': first_date_of_14_days,
        'last_date_of_14_days': last_date_of_14_days,
        'date': date_list,
        'date_last14': date_last14,
        'activity_label': activity_label,
        'data': sum_value_at_date
    }


    return render(request, 'hydration/hydration_history.html', context=context)
