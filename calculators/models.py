from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# User = get_user_model()

# Create your models here.
class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bmi')
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

