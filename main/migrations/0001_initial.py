# Generated by Django 3.1.6 on 2021-03-02 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_job', models.CharField(max_length=255, verbose_name='Название структур: ')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_file', verbose_name='Фото: ')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО: ')),
                ('job', models.CharField(max_length=255, verbose_name='Должность: ')),
                ('vnut_atc', models.IntegerField(verbose_name='Внут.АТС: ')),
                ('gor_atc', models.CharField(max_length=8, verbose_name='Гор.АТС: ')),
                ('email', models.EmailField(max_length=254, verbose_name='Email: ')),
                ('room', models.IntegerField(verbose_name='Кабинет: ')),
                ('name_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.name_job')),
            ],
        ),
    ]
