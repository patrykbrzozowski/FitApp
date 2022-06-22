from django.contrib import admin
from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('BMI_calculator/', views.BMI_calculator, name='BMI_calculator'),
]
