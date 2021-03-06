from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')


def achievements(request):
    return render(request, 'achievements.html')


def teacher_intro(request):
    return render(request, 'teacher_intro.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
           
            else:
                user = User.objects.create_user(
                    username=username, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request, ' Password not Matching.....')
            return redirect('signup')
        return redirect('home')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid User')
            return redirect('login')
        

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')