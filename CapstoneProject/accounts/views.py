from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def log_in(request:HttpRequest):

    msg = None

    if request.method == 'POST':
        user : User = authenticate(request, username=request.POST['username'], password=request.POST["password"])
        login(request, user)
        return redirect("accounts:no_permission")
    else:
        msg = 'username or password is incorrect'

    return render(request, 'accounts/log_in.html', {'msg' : msg})


def log_out(request:HttpRequest):

    logout(request)


    return redirect('accounts:no_permission')


def no_permission(request:HttpRequest):



    return render(request, 'accounts/no_permission.html')