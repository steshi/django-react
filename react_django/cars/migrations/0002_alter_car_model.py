# Generated by Django 4.1.3 on 2022-11-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=40, verbose_name='First name'),
        ),
    ]
