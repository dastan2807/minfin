# Generated by Django 3.1.6 on 2021-03-16 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_person_name_otdel'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name_otdel',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='main.name_otdel'),
            preserve_default=False,
        ),
    ]