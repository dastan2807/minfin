# Generated by Django 3.1.6 on 2021-03-24 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npa', '0005_auto_20210323_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npadocument',
            name='category',
        ),
        migrations.DeleteModel(
            name='NpaCategory',
        ),
    ]
