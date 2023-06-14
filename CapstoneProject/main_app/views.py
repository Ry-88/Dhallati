from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.



def home(request:HttpRequest):


    return render(request, 'main_app/home.html')


def not_found(request:HttpRequest):



    return render(request, 'main_app/not_found.html')


def request_add(request:HttpRequest):



    return render(request, 'main_app/request_add.html')


def request_detail(request:HttpRequest):



    return render(request, 'main_app/request_detail.html')


def request_tracking(request:HttpRequest):



    return render(request, 'main_app/request_tracking.html')