from django.contrib import admin
from .models import *

# class BookList_admin(admin.ModelAdmin):
#     list_display = ['name','author','available']
#     list_display_link = ['name']

# class Student_admin(admin.ModelAdmin):
#     list_display = ['name','user','ph_number']
#     list_display_link=['Name']

# class Issuebook_admin(admin.ModelAdmin):
#     list_display = ['Student_name','Book_name','issue_date','expiry_date']
#     list_display_link=['Student_name']


admin.site.register(BookList)
admin.site.register(Student)
admin.site.register(issuedbook)
