# Generated by Django 3.2.9 on 2021-11-07 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0016_auto_20211106_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='Student_name',
            new_name='student_name',
        ),
    ]