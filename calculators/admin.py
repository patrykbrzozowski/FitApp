from django.contrib import admin
from .models import BMI

# Register your models here.
class BmiAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'bmi', 'date')

admin.site.register(BMI, BmiAdmin)
