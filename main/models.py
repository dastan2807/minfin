from django.db import models
from django.contrib.auth.models import User

class Name_job(models.Model):
    name_job = models.CharField('Название структур ', max_length=255)

    def __str__(self):
        return self.name_job

    class Meta:
        verbose_name = 'Добавление управлений'
        verbose_name_plural = 'Добавление управлений'

class Name_otdel(models.Model):
    name_job = models.ForeignKey(Name_job, related_name="name_job_otdel", on_delete=models.CASCADE, verbose_name='Название структур')
    name_otdel = models.CharField('Название отдела', max_length=255)

    def __str__(self):
        return self.name_otdel

    class Meta:
        verbose_name = 'Добавление отделов'
        verbose_name_plural = 'Добавление отделов'

class Rukovodstva(models.Model):
    rukovodstva = models.CharField('Название: ', max_length=255)

    def __str__(self):
        return self.rukovodstva

    class Meta:
        verbose_name = 'Добавление звание руководства '
        verbose_name_plural = 'Добавление звание руководства'

class MainPersonUser(models.Model):
    name_job = models.OneToOneField(Name_job, related_name="main_job", on_delete = models.CASCADE)
    image = models.ImageField('Фото ', upload_to='image_file', blank=True, null = True)
    name = models.CharField('ФИО ', max_length=255)
    job = models.CharField(default='Начальник', max_length=100, blank=True, null=True)
    vnut_atc = models.IntegerField('Внут.АТС ')
    phone = models.CharField('Тел ', max_length=255)
    email = models.EmailField('Email ')
    room = models.CharField('Кабинет ', max_length=10, blank=True, null=True)
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    rukovodstva = models.ForeignKey(Rukovodstva, on_delete = models.CASCADE, blank=True, null=True, related_name='rukovodstva')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление начальников'
        verbose_name_plural = 'Добавление начальников'

class Person(models.Model):
    name_otdel = models.ForeignKey(Name_otdel, on_delete = models.CASCADE, default=1, related_name='person_otdel')
    image = models.ImageField('Фото ', upload_to='image_file', blank=True, null = True  )
    name = models.CharField('ФИО ', max_length=255)
    job = models.CharField('Должность ', max_length=255)
    vnut_atc = models.CharField('Внут.АТС', max_length=50)
    gor_atc = models.CharField('Гор.АТС ', max_length=255)
    email = models.EmailField('Email ')
    room = models.CharField('Кабинет ', max_length=10)
    index = models.IntegerField('Индекс',null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление сотрудников'
        verbose_name_plural = 'Добавление сотрудников'