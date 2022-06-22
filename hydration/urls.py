from django.urls import path

from hydration import views

app_name = 'hydration'

urlpatterns = [
    path('water_list/', views.WaterListView.as_view(), name='water_list'),
    path('water_detail/<pk>', views.WaterDetailView.as_view(), name='water_detail'),
    path('water_create/', views.WaterCreateView.as_view(), name='water_create'),
    path('water_update/<pk>', views.WaterUpdateView.as_view(), name='water_update'),
    path('water_delete/<pk>', views.WaterDeleteView.as_view(), name='water_delete'),
    path('water_chart/', views.WaterChartView, name='water_chart'),
    path('water_history/', views.WaterHistoryView, name='water_history'),
]