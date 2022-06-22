import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Water(models.Model):
    class WTypes(models.IntegerChoices):
        FIL = 1, "FILIŻANKA (100ML)"
        SZK = 2, "SZKLANKA (200ML)"
        DUK = 3, "DUŻY KUBEK (400ML)"
        BUT0_5 = 4, "BUTELKA 0,5 L"
        BUT1 = 5, "BUTELKA 1 L"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='water')
    value = models.PositiveSmallIntegerField(choices=WTypes.choices)
    real_value = models.IntegerField(null=True)
    date = models.DateTimeField()
    created_at_date = models.DateTimeField(auto_now_add=True)
    created_at_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'Woda {self.id} - {self.value} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'water'