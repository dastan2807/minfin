# Generated by Django 3.1.6 on 2021-03-16 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_name_otdel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name_job',
        ),
        migrations.AddField(
            model_name='person',
            name='name_otdel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.name_otdel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='name_otdel',
            name='name_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.name_job', verbose_name='Название структур'),
        ),
    ]
