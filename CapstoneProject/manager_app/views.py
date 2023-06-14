from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main_app.models import Catagory,SubCatagory


# Create your views here.
def  index_page(request:HttpRequest):
    return render(request,"manager_app/manager.html")