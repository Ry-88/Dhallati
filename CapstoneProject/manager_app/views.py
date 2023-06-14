from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main_app.models import Catagory,SubCatagory


# Create your views here.
'''
def  index_page(request:HttpRequest):
    return render(request,"manager_app/manager.html")
def add_category(request:HttpRequest):
    if request.method=="404":
        new_category=Catagory(name=request.POST["categoryname"])
        return redirect()
    return render(request,"")

def add_subcategory(request:HttpRequest,category_id):

    category=Catagory.objects.get(id=category_id)
    if request.method=="404":
        new_subCategory=Catagory(category=category,name=request.POST["categoryname"])
        return redirect()
        '''