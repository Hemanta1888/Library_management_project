# Generated by Django 3.2.5 on 2021-11-05 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0011_remove_student_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='student_id',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='name',
            new_name='student_name',
        ),
    ]