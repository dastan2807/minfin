# Generated by Django 3.1.6 on 2021-04-15 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210412_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rukovodstva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rukovodstva', models.CharField(max_length=255, verbose_name='Название: ')),
            ],
            options={
                'verbose_name': 'Добавление руководства ',
                'verbose_name_plural': 'Добавление руководства',
            },
        ),
        migrations.AddField(
            model_name='mainpersonuser',
            name='rukovodstva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.rukovodstva'),
        ),
    ]