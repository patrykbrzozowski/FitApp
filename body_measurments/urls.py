from django.urls import path

from body_measurments import views

app_name = 'body_measurements'

urlpatterns = [
    path('body_measurements_list/', views.BodyMeasurementsListView.as_view(), name = 'body_measurements_list'),
    path('body_measurements_detail/<pk>', views.BodyMeasurementsDetailView.as_view(), name='body_measurements_detail'),
    path('body_measurements_create/', views.BodyMeasurementsCreateView.as_view(), name='body_measurements_create'),
    path('body_measurements_update/<pk>', views.BodyMeasurementsUpdateView.as_view(), name='body_measurements_update'),
    path('body_measurements_delete/<pk>', views.BodyMeasurementsDeleteView.as_view(), name='body_measurements_delete'),
    path('body_measurements_chart/', views.BodyMeasurementsViewChart, name='body_measurements_chart'),
    path('body_measurements_get_chart/', views.BodyMeasurementsGetChart, name='body_measurements_get_chart'),

    path('body_circuits_list/', views.BodyCircuitsListView.as_view(), name = 'body_circuits_list'),
    path('body_circuits_detail/<pk>', views.BodyCircuitsDetailView.as_view(), name='body_circuits_detail'),
    path('body_circuits_create/', views.BodyCircuitsCreateView.as_view(), name='body_circuits_create'),
    path('body_circuits_update/<pk>', views.BodyCircuitsUpdateView.as_view(), name='body_circuits_update'),
    path('body_circuits_delete/<pk>', views.BodyCircuitsDeleteView.as_view(), name='body_circuits_delete'),

    path('goal_create/', views.GoalsCreateView.as_view(), name='goal_create'),

    #path('body_circuits_chart/', views.BodyCircuitsViewChart, name='body_circuits_chart'),
    #path('body_circuits_get_chart/', views.BodyCircuitsGetChart, name='body_circuits_get_chart'),
]