from django.db import models
import datetime
from django.contrib.auth.models import User

class BookList(models.Model):
    Book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField()

    def __str__(self):
        return self.Book_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    email = models.EmailField()
    ph_number = models.IntegerField()

    def __str__(self):
        return self.student_name


def expiry_date():
    return datetime.datetime.today()+datetime.timedelta(days=15)

class issuedbook(models.Model):
    student_name = models.CharField(max_length=100)
    Book_name = models.CharField(max_length=100) 
    issue_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry_date)

    def __str__(self):
        return self.student_name

    
