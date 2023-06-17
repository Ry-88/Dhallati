from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import RequestLostItem, Catagory, SubCatagory
# Create your views here.




def home(request: HttpRequest):


#    if request.method == 'POST':
#
#        if 'track' in request.POST:
#            all_track = Class.objects.all()
#            track_request= Class.objects.get(id=request.POST['request_number'])
#
#        if 'help' in request.POST:
#            new_help = Class(first_name=request.POST['first_name'],
#                             last_name=request.POST['last_name'],
#                             email=request.POST['email'],
#                             message=request.POST['message'])
#            new_help.save()
#
    return render(request, 'main_app/home.html')



def not_found(request: HttpRequest):

    return render(request, 'main_app/not_found.html')



def category(request: HttpRequest):
    categories = Catagory.objects.all()
    return render(request,'main_app/category_for_add_request_add.html',{"categories":categories})


def request_add(request: HttpRequest,category_id):

    category=Catagory.objects.get(id=category_id)
    sub_category=SubCatagory.objects.filter(category=category)
    
    if request.method == "POST":
        
        if "image" in request.FILES:
            new_request = RequestLostItem(catagory=category,Sub_catagory= SubCatagory.objects.get(id=request.POST["sub_category"]), color=request.POST["color"], 
                                          place=request.POST["place"], description=request.POST["description"], 
                                          image=request.FILES["image"],
                                          email=request.POST["email"],
                                          name=request.POST["name"],
                                          phone_number=request.POST["phone_number"])

        
        new_request = RequestLostItem(catagory=category,Sub_catagory= SubCatagory.objects.get(id=request.POST["sub_category"]) ,color=request.POST["color"], 

                                          place=request.POST["place"], description=request.POST["description"],
                                          email=request.POST["email"],
                                          name=request.POST["name"],
                                          phone_number=request.POST["phone_number"])
        

        new_request.save()
        return redirect("main_app:home")

    return render(request, 'main_app/request_add.html', {"category":category,"sub_category":sub_category})


    

def request_detail(request: HttpRequest,lost_id):

    requests = RequestLostItem.objects.get(id=lost_id)

    return render(request, 'main_app/request_detail.html', {'requests' : requests})


def request_tracking(request: HttpRequest, track_id):

    tracking = RequestLostItem.objects.get(id=track_id)

    return render(request, 'main_app/request_tracking.html', {'tracking' : tracking})
