# Generated by Django 3.2.5 on 2021-11-05 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0012_auto_20211105_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='book_name',
            new_name='bookname',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='student_name',
            new_name='studentname',
        ),
    ]
