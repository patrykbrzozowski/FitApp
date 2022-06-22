from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BodyMeasurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='body_measurements')
    weight = models.FloatField()
    height = models.FloatField()
    date = models.DateField()
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pomiary ciała: {self.wieght} kg - {self.height} cm'

    class Meta:
        verbose_name_plural = 'body measurements'

class BodyCircuits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='body_circuits')
    neck = models.FloatField()  # szyja
    hips = models.FloatField()    # biodra
    chest = models.FloatField()    # kaltka piersiowa
    biceps = models.FloatField()    # biceps
    thigh = models.FloatField()   # udo
    waist = models.FloatField() # talia
    calf = models.FloatField() # lydka
    belly = models.FloatField()    # brzuch
    date = models.DateField()
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Obwody ciała: klatka {self.chest} cm, biceps: {self.biceps} cm'

    class Meta:
        verbose_name_plural = 'body circuits'

class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    weight_goal = models.FloatField()
    week_rate = models.FloatField(default=0.5)
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cel: {self.wieght} kg tygodniowo'

    class Meta:
        verbose_name_plural = 'goals'