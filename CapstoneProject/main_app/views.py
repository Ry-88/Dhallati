from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.



def home(request:HttpRequest):



    if request.method == 'POST':

        if 'track' in request.POST:
            all_track = Class.objects.all()
            track_request= Class.objects.get(id=request.POST['request_number'])

        if 'help' in request.POST:
            new_help = Class(first_name=request.POST['first_name'],
                             last_name=request.POST['last_name'],
                             email=request.POST['email'],
                             message=request.POST['message'])
            new_help.save()

    return render(request, 'main_app/home.html')


def not_found(request:HttpRequest):



    return render(request, 'main_app/not_found.html')


def request_add(request:HttpRequest):



    return render(request, 'main_app/request_add.html')


def request_detail(request:HttpRequest, request_id):

    


    return render(request, 'main_app/request_detail.html')


def request_tracking(request:HttpRequest):



    return render(request, 'main_app/request_tracking.html')