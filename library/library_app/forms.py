from django import forms
from .models import *
from django.contrib.auth.models import User

class IssueBookForm(forms.Form):
    BookName = forms.ModelChoiceField(queryset=BookList.objects.all(), empty_label="Name of the book", label="Book")
    StudentName = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Name of the Student", label="Student")

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']