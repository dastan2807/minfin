# Generated by Django 3.1.6 on 2021-04-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profcom', '0005_profcom_full_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfOpros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateField(verbose_name='Дата публикации')),
                ('mac', models.CharField(max_length=50, verbose_name='Мак адрес')),
            ],
        ),
        migrations.DeleteModel(
            name='ProfcomOpros',
        ),
    ]