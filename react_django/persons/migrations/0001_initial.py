# Generated by Django 4.1.3 on 2022-11-09 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='First name')),
                ('surname', models.CharField(max_length=255, verbose_name='Last name')),
                ('driverlicensenum', models.CharField(max_length=12)),
                ('birthdate', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
