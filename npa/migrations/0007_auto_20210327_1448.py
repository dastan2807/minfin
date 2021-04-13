# Generated by Django 3.1.6 on 2021-03-27 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('npa', '0006_auto_20210324_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='NpaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='NpaDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Названия документа')),
                ('number', models.CharField(max_length=255, verbose_name='Номер документа')),
                ('pdff', models.FileField(upload_to='pdf_file', verbose_name='PDF')),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npa.npacategory', verbose_name='Категория')),
            ],
        ),
        migrations.DeleteModel(
            name='NpaDocument',
        ),
    ]
