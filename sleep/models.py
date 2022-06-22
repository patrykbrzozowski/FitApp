from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sleep')
    date = models.DateField()
    duration_time = models.FloatField(null=False)

    class Meta:
        verbose_name_plural = 'sleep'

