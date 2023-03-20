from django.shortcuts import render, redirect
from .models import ExpenseRecord
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    feature1 = ExpenseRecord.objects.all()
    return render(request, 'index.html', {'feature': feature1})

def first(request):
    return render(request, 'first.html')

def next_page(request):
    return render(request, 'next.html')

def register(request):
    if request.method == 'POST':
    
    # if request.POST.get('submit') == 'SignUp':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password) 
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password is not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

    
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logoutuser(request):
    logout(request)
    return redirect('login')
