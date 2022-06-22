from django.urls import path

from activities import views

app_name = 'activities'

urlpatterns = [
    path('activities_list/', views.ActivityListView.as_view(), name = 'activities_list'),
    path('all_activities_list/', views.ActivityListViewAll, name = 'all_activities_list'),
    path('activities_detail/<pk>', views.ActivityDetailView.as_view(), name='activities_detail'),
    path('activities_create/', views.ActivityCreateView.as_view(), name='activities_create'),
    path('activities_update/<pk>', views.ActivityUpdateView.as_view(), name='activities_update'),
    path('activities_delete/<pk>', views.ActivityDeleteView.as_view(), name='activities_delete'),
    path('activities_chart/', views.ActivityChartView, name='activities_chart'),
    #path('activities_history/', views.ActivityHistoryView, name='activities_history'),
]