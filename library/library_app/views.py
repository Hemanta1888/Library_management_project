from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.models import Group

from .forms import *
from .models import *

def homepage(request):
    return render(request,'app_template/home.html')

@login_required
def add_book(request):
    submitted=False
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        available = request.POST['available']
        books = BookList.objects.create(Book_name=name, author=author,available=available)
        books.save()
        submitted = True
    return render(request,'app_template/AddBook.html',{
        'submit':submitted
    })
@login_required
def view_book(request):
    books=BookList.objects.all()
    return render(request,'app_template/viewbook.html',{
        'book':books
    })

@login_required
def issue_book(request):
    form = IssueBookForm()
    submitted = False
    if request.method == 'POST':
        form  = IssueBookForm(request.POST)
        if form.is_valid():
            model_data = issuedbook()
            model_data.Book_name = request.POST['BookName']
            model_data.student_name = request.POST['StudentName']
            model_data.save()
            submitted = True

    return render(request,'app_template/issue_book.html',{
        'submit':submitted,
        'form':form
    })


@login_required
def view_issuedBook(request):
    issue = issuedbook.objects.all()
    issue_book_details = []
    for data in issue:
        issuedate=str(data.issue_date.day)+'-'+str(data.issue_date.month)+'-'+str(data.issue_date.year)
        expdate=str(data.expiry_date.day)+'-'+str(data.expiry_date.month)+'-'+str(data.expiry_date.year)
        today = datetime.date.today()
        issue_date = data.issue_date
        No_of_days = today-issue_date
        total_days = No_of_days.days
        fine = 0
        if total_days > 15:
            days = total_days-15
            fine = days * 10
        books = list(BookList.objects.filter(Book_name=data.Book_name))
        students = list(Student.objects.filter(Book_name=data.student_name))
        i = 0
        for l in books:
            info = (students[data].user,students[data].email,books[data].name,books[data].author,issuedate,expdate,fine)
            i= i + 1
            issue_book_details.append(info)
        return render(request, "app_template/view_issuedbook.html", {
            'issuedBooks':issue, 
            'IssueBook_details':issue_book_details
                })
def student_issuedbook(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuebook = issuedbook.objects.filter(Book_name = student[0].student_name)
    list1 = []
    list2 = []

    for i in issuebook:
        books = BookList.objects.filter(Book_name=i.Book_name)
        for book in books:
            t=(request.user, book.name,book.author)
            list1.append(t)

        days=(datetime.date.today()-i.issue_date)
        d=days.days
        fine=0
        if d>15:
            days=d-15
            fine=days*10
        t=(issuebook[0].issued_date, issuebook[0].expiry_date, fine)
        list2.append(t)
    return render(request,'app_template/student_issuedbooks.html',{
        'list1':list1, 
        'list2':list2
        })
def student_registration(request):
    submitted = False
    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nickname = request.POST['name']
        email = request.POST['email']
        confirm_email = request.POST['confirm_email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password != confirmPassword:
            passwordIncorrect = True
        if email != confirm_email:
            emailIncorrect = True
            return render(request,'app_template/incorrect.html',{
                'incorrectPassword':passwordIncorrect,
                'incorrectemail':emailIncorrect
            })
        phone_no = str(phone)
        if len(phone_no) < 10:
            raise ValidationError("The phone number should have 10 digits. ")
        user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        student_data = Student.objects.create(user= user,email=confirm_email,ph_number = phone,student_name=nickname)
        user.save()
        student_data.save()
        submitted = True
        return HttpResponseRedirect("/studentlogin")
    return  render(request,'app_template/studentregd.html',{
        'submit':submitted,
    })

def student_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/student_homepage")
        else:
            submitted = True
            return render(request,"app_template/invalidlogin.html",{
                'submit':submitted
            })
    return render(request, "app_template/studentLogin.html")

@login_required
def view_student(request):
    students = Student.objects.all()
    return render(request,'app_template/viewstudents.html',{
        'students':students
    })

def student_homepage(request):
    return render(request,'app_template/student_homepage.html')


def delete_book(request,bookname):
    book = BookList.objects.filter(name=bookname )
    book.delete()
    return redirect("/viewbook")

def delete_student(request,studentname):
    student = Student.objects.filter(name = studentname)
    student.delete()
    return redirect("/viewstudent")

def logout(request):
    return render(request,'app_template/logout.html')


def adminsignup_view(request):
    form=AdminSigupForm()
    if request.method=='POST':
        form=AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('accounts/login/')
    return render(request,'app_template/adminsignup.html',{'form':form})