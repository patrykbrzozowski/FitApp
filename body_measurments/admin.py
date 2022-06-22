from django.contrib import admin
from body_measurments.models import BodyCircuits, BodyMeasurements, Goals

# Register your models here.
admin.site.register(BodyCircuits)
admin.site.register(BodyMeasurements)
admin.site.register(Goals)