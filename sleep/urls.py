from django.urls import path

from sleep import views

app_name = 'sleep'

urlpatterns = [
    path('sleep_list/', views.SleepListView.as_view(), name='sleep_list'),
    path('sleep_detail/<pk>', views.SleepDetailView.as_view(), name='sleep_detail'),
    path('sleep_create/', views.SleepCreateView.as_view(), name='sleep_create'),
    path('sleep_update/<pk>', views.SleepUpdateView.as_view(), name='sleep_update'),
    path('sleep_delete/<pk>', views.SleepDeleteView.as_view(), name='sleep_delete'),
    path('sleep_chart/', views.SleepChartView, name='sleep_chart'),
    # path('sleep_history/', views.SleepHistoryView, name='sleep_history'),
]