from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    class ATypes(models.IntegerChoices):
        BIE = 1, "Bieganie"
        ROW = 2, "Jazda na rowerze"
        TRE = 3, "Trening siłowy"
        PIL = 4, "Piłka nożna"
        KOS = 5, "Koszykówka"
        BAD = 6, "Badminton"
        SKA = 7, "Skakanka"
        JOG = 8, "Joga"
        TEN = 9, "Tenis"
        BOK = 10, "Boks"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity')
    type = models.PositiveSmallIntegerField(choices=ATypes.choices, default=3)
    duration_time = models.FloatField()
    date = models.DateField()
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Aktywność {self.id} - {self.get_type_display} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'activities'
