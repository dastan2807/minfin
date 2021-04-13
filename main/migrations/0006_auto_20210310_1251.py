# Generated by Django 3.1.6 on 2021-03-10 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20210303_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPersonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image_file', verbose_name='Фото ')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО ')),
                ('vnut_atc', models.IntegerField(verbose_name='Внут.АТС ')),
                ('phone', models.CharField(max_length=255, verbose_name='Тел ')),
                ('email', models.EmailField(max_length=254, verbose_name='Email ')),
                ('login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name_job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.name_job')),
            ],
        ),
        migrations.DeleteModel(
            name='MainPerson',
        ),
    ]
