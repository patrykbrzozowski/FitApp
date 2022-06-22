from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sleep', null=True)
    date = models.DateField(null=True)
    duration_time = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'sleep'

