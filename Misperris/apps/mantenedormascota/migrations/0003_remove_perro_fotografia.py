# Generated by Django 2.1.2 on 2018-11-06 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedormascota', '0002_auto_20181105_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='fotografia',
        ),
    ]