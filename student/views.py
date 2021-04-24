from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import studentdata
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Avg,Min,Max


# Create your views here.
def home(request):
    return render(request, 'home.html')


def details(request):
    student_data = studentdata.objects.all
    return render(request, 'details.html', {'student_data': student_data})


def create(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/details')
    form = studentForm()
    return render(request, 'create.html', {'form': form})


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('password1')
        if password==confirmpassword:
           user=User.objects.create_superuser(username=username,email=email,password=password)
           user.save()
           send_mail('login link',
                   'User Registered Successfully'
                   'http://127.0.0.1:8000/student/login/',
                   settings.EMAIL_HOST_USER,
                   [email])
           return redirect('/student/login/')
    else:
        print('enter valid password')
    return render(request,'register.html')


def edit(request, id):
    student_data = studentdata.objects.get(id = id)
    form = studentForm(instance=student_data)
    return render(request, 'update.html', {'form': form, 'id': id})


def update(request, id):
    student_data = studentdata.objects.get(id = id)
    form = studentForm(request.POST, instance=student_data)
    if form.is_valid():
        form.save()
        return redirect('/student/details')
    return render(request, 'update.html', {'form': form})


def delete1(request, id):
    student_data = studentdata.objects.get(id = id)
    student_data.delete()
    return redirect('/student/details/')


def us_login(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request,user)

            return redirect('/student/details/')
    return render(request, 'login.html', {})


def us_logout(request):
    logout(request)
    return redirect('/student/login/')


def sqlquaries(request):
     TOTALSTUDENTS = studentdata.objects.all().count()
     AVERAGE = studentdata.objects.aggregate(Avg('Markspercentage'))
     A = AVERAGE['Markspercentage__avg']
     MINIMUM =studentdata.objects.aggregate(Min('Markspercentage'))
     B = MINIMUM['Markspercentage__min']
     MAXIMUM = studentdata.objects.aggregate(Max('Markspercentage'))
     C = MAXIMUM['Markspercentage__max']
     GREATER = studentdata.objects.filter(Markspercentage__gte=70).count()
     FAIL = studentdata.objects.filter(Markspercentage__lt=70).count()

     s = [TOTALSTUDENTS,A,B,C,GREATER,FAIL]
     z = ['TOTALSTUDENTS', 'AVERAGE', 'MINIMUM', 'MAXIMUM', 'GREATER', 'FAIL']
     return render(request, 'info.html', {'z':z, 's': s})
