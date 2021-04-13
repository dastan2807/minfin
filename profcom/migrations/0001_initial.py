# Generated by Django 3.1.6 on 2021-03-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profcom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profcom_file', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Текст')),
                ('data', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]