# Generated by Django 3.2.5 on 2021-11-05 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_auto_20211105_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Email',
        ),
    ]
