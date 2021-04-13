# Generated by Django 3.1.6 on 2021-03-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profcom', '0003_auto_20210325_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfcomOpros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]
