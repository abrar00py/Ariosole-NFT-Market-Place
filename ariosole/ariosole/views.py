import imp
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from digitalart.models import digitalart
from musicart.models import musicart
def home(request):
    return render(request, 'index.html')

def Login(request):
    if request.user.is_active:
        messages.warning(request, "your are already logged in")
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get('Username')
            passwd = request.POST.get('Password')

            user = authenticate(request ,username=name, password=passwd)
            print(name,passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                print("hi")
                return redirect("/")
            else:
                messages.error(request, "invalid username and password")
                a="username and password is error"
                return redirect("/login")
        
        return render(request, "registration/login.html")

def contact(request):
    return render(request, 'author.html')

def explore(request):
    digital_art = digitalart.objects.all()
    context = {
        "digitalart":digital_art
    }
    return render(request, 'explore.html', context)

def Musicart(request):
    music = musicart.objects.all()
    context = {
        "musicart":music
    }
    return render(request,"musicart.html", context)
