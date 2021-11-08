from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('addbooks',views.add_book,name= 'addbook'),
    path('viewbook',views.view_book,name='viewbook'),
    path('issuebook',views.issue_book,name='IssueBook'),
    path('issuedbook',views.view_issuedBook,name='issuedbook'),
    path('studentregister',views.student_registration,name='studentregister'),
    path('studentlogin',views.student_login,name='studentlogin'),
    path('viewstudent',views.view_student,name='viewstudents'),
    path('student_homepage',views.student_homepage,name='StudentHomepage'),
    path('student_issuedbook',views.student_issuedbook,name='student_issuedbook'),
    path('deletebook/<str:bookname>',views.delete_book,name='deletebook'),
    path('deletestudent/<str:studentname>',views.delete_student,name='deletestudent'),
    path('logout',views.logout,name='logout'),
    path('adminsignup', views.adminsignup_view,name='adminsignup'),
]