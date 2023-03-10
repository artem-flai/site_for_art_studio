# Generated by Django 3.2.9 on 2021-11-20 13:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_picture', models.CharField(max_length=180)),
                ('foto', models.ImageField(upload_to='picture')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='MasterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=180)),
                ('date_mk', models.DateField(default=datetime.date(2021, 11, 20))),
                ('time_mk', models.TimeField(default=datetime.time)),
                ('price', models.CharField(max_length=80)),
                ('view_of_clients', models.CharField(max_length=120)),
                ('foto', models.ImageField(upload_to='picture')),
                ('activation', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Мастер-классы',
                'verbose_name_plural': 'Мастер-классы',
            },
        ),
        migrations.CreateModel(
            name='MasterClass_Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_picture', models.CharField(max_length=80)),
                ('name_guest', models.CharField(max_length=80)),
                ('tel_guest', models.DecimalField(decimal_places=0, max_digits=9)),
                ('email_guest', models.EmailField(max_length=254)),
                ('master_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='picture.masterclass')),
                ('picture_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='picture.gallery_picture')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
