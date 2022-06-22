from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('calculators/', include('calculators.urls')),
    path('hydration/', include('hydration.urls')),
    path('activities/', include('activities.urls')),
    path('sleep/', include('sleep.urls')),
    path('body_measurements/', include('body_measurments.urls')),
]
