# Generated by Django 3.2.9 on 2021-11-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0015_student_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklist',
            old_name='name',
            new_name='Book_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='Book_name',
            field=models.CharField(max_length=100),
        ),
    ]
