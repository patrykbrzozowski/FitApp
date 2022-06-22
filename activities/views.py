from calendar import weekday
from datetime import date, timedelta, datetime
from re import template
from urllib import request
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from activities.forms import ActivityForm
from activities.models import Activity

# Create your views here.
class ActivityListView(ListView):
    model = Activity
    paginate_by = 100
    template_name = 'activities/activities_list.html'
    extra_context = {'today': date.today().strftime('%d/%m/%Y')}

    def get_queryset(self):
        user = self.request.user
        return Activity.objects.filter(user=user, date=date.today())

class ActivityDetailView(DeleteView):
    model = Activity
    template_name = 'activities/activities_detail.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Activity.objects.filter(user=user)

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activities_form.html'
    extra_context = {}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Aktywność została dodana!')
        return reverse_lazy('activities:activities_list')

class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activities_form.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Activity.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Aktywność została zaaktualizowana!')
        return reverse('activities:activities_detail', kwargs={'pk': self.object.pk})

class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/activities_confirm_delete.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return Activity.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Aktywność została usunięta!')
        return reverse_lazy('activities:activities_list')

def ActivityChartView(request):
    all_activities_today = Activity.objects.filter(date=date.today(), user=request.user)

    all_activities = Activity.objects.filter(user=request.user).order_by('date')

    type_list = [activity_type['type'] for activity_type in Activity.objects.filter(user=request.user).values('type')]

    print(type_list)

    date_list = [activity_date['date'] for activity_date in Activity.objects.filter(user=request.user).values('date').order_by('date').distinct()]

    today = datetime.now()
    n_days_ago = today - timedelta(days=14)

    date_last14 = []

    for i in range(14, -1 ,-1):
        n_days_ago = today - timedelta(days=i)
        date_last14.append(n_days_ago.date())

    #print("Daty",date_last14)

    sum_value_at_date = []
    activity_label = []

    for activity in all_activities_today:
        activity_label.append(activity.type)

    for activity_date in date_last14:
        activities_tot = Activity.objects.filter(user=request.user).aggregate(s=Sum('duration_time', filter=Q(date=activity_date)))['s']
        if activities_tot is None:
            sum_value_at_date.append(0)
        else:
            sum_value_at_date.append(activities_tot)

    print(sum_value_at_date)

    first_date_of_14_days = date_last14[0]
    last_date_of_14_days = date_last14[-1]

    context = {
        'all_activities_today': all_activities_today,
        'all_activities': all_activities,
        'first_date_of_14_days': first_date_of_14_days,
        'last_date_of_14_days': last_date_of_14_days,
        'date': date_list,
        'date_last14': date_last14,
        'activity_label': activity_label,
        'data': sum_value_at_date
    }

    return render(request, 'activities/activities_chart.html', context=context)


# def ActivityChartView(request):
#     visuals_data = {
#             'chart_type': 'bar',
#             'labels': [],
#             'datasets': [
#                 {
#                     'label': 'x',
#                     'backgroundColor': '#3c9c85',
#                     'stack': 'limit',
#                     'data': []
#                 }
#             ],
#         }

#     activities_list = [activity for activity in Activity.objects.all()]

#     for activity in activities_list:
#         activity_data = {
#             'label': activity.type,
#             'backgroundColor': '#b60000',
#             'borderColor': '#b60000',
#             'data': [activity.duration_time]
#         }
#         visuals_data['datasets'].append(activity_data)
        
#     return JsonResponse(visuals_data)

# class ActivityListViewAll(ListView):
#     model = Activity
#     paginate_by = 100
#     template_name = 'activities/all_activities_list.html'

#     group_rec = Activity.objects.values('date').annotate(count=Sum('duration_time')).values('date', 'count').order_by('date')

#     date_list = [activity_date['date'] for activity_date in Activity.objects.values('date').order_by('-date').distinct()]
#     sum_value_at_date = []

#     for activity_date in date_list:
#         activities_tot = Activity.objects.aggregate(s=Sum('duration_time', filter=Q(date=activity_date)))['s']
#         sum_value_at_date.append(activities_tot)

#     zipped_data = zip(date_list, sum_value_at_date)


#     extra_context = {
#         'today': date.today().strftime('%d/%m/%Y'), 
#         'date_list': date_list,
#         'zipped_data': zipped_data,
#     }

#     print(zipped_data)

#     def get_queryset(self):
#         user = self.request.user
#         return Activity.objects.filter(user=user).order_by('-date')
#         # date_list = [activity_date['date'] for activity_date in Activity.objects.values('date').distinct()]
#         # sum_value_at_date = []
#         # for activity_date in date_list:
#         #     activities_tot = Activity.objects.aggregate(s=Sum('duration_time', filter=Q(date=activity_date)))['s']
#         #     sum_value_at_date.append(activities_tot)
#         # return sum_value_at_date

def ActivityListViewAll(request):


    #group_rec = Activity.objects.values('date').annotate(count=Sum('duration_time')).values('date', 'count').order_by('date')

    date_list = [activity_date['date'] for activity_date in Activity.objects.filter(user=request.user).values('date').order_by('-date').distinct()]
    sum_value_at_date = []

    all_activities = Activity.objects.filter(user=request.user).order_by('-date')

    for activity_date in date_list:
        activities_tot = Activity.objects.filter(user=request.user).aggregate(s=Sum('duration_time', filter=Q(date=activity_date)))['s']
        sum_value_at_date.append(activities_tot)

    zipped_data = zip(date_list, sum_value_at_date)


    context = {
        'today': date.today().strftime('%d/%m/%Y'), 
        'all_activities': all_activities,
        'date_list': date_list,
        'zipped_data': zipped_data,
    }

    print(zipped_data)

    

    return render(request, 'activities/all_activities_list.html', context=context)