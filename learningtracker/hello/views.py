from django.shortcuts import render, redirect
from .models import Course, Student, Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Home Page (Restricted)
@login_required
def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students
    }
    return render(request, 'hello/home.html', context)
# Register Page
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'hello/register.html')
# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'hello/login.html')
# Logout
def logout_view(request):
    logout(request)
    return redirect('login')




