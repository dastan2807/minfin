from django.db import models
from django.contrib.auth.models import User
from main.models import Name_job

class Jurnal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name_job = models.ForeignKey(Name_job, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    text_prich = models.CharField(max_length=255, verbose_name='Причина')
    time_exit = models.CharField(max_length=25, verbose_name='Отметка об убытии')
    time_enter = models.CharField(max_length=25, verbose_name='Отметка о прибытии')

    class Meta:
        verbose_name = 'Журнал выездов (не лезьте)'
        verbose_name_plural = 'Журнал выездов (не лезьте)'

