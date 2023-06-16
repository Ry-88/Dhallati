from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import RequestLostItem, Catagory, SubCatagory
# Create your views here.



def home(request: HttpRequest):


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


def not_found(request: HttpRequest):

    return render(request, 'main_app/not_found.html')


def request_add(request: HttpRequest):

    catagories = Catagory.objects.all()
    sub_catagory = SubCatagory.objects.filter()
    requests = RequestLostItem.objects.all()
    if request.method == "POST":
        requestItem = RequestLostItem.objects.get(id=request.POST["publisher"])

        if "image" in request.FILES:
            new_request = RequestLostItem(catagory=request.POST["catagory"], color=request.POST["color"], 
                                          place=request.POST["place"], description=request.POST["description"], 
                                          image=request.FILES["image"],status=request.POST["status"], 
                                          is_read=request.POST["is_read"])
        else:
            new_request = RequestLostItem(catagory=request.POST["catagory"], color=request.POST["color"], 
                                          place=request.POST["place"],description=request.POST["description"],
                                          status=request.POST["status"], is_read=request.POST["is_read"])
        new_request.save()
        return redirect("main_app:home")

    return render(request, 'main_app/request_add.html', {"requests":requests})


    

def request_detail(request: HttpRequest):

    return render(request, 'main_app/request_detail.html')


def request_tracking(request: HttpRequest):

    return render(request, 'main_app/request_tracking.html')
