# Generated by Django 3.1.6 on 2021-03-16 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_mainpersonuser_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name_otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_otdel', models.CharField(max_length=255, verbose_name='Название отдела')),
                ('name_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.name_job', verbose_name='Название структур ')),
            ],
        ),
    ]
