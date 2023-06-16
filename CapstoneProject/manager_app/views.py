from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main_app.models import Catagory,SubCatagory

from django.core import serializers
import json

# Create your views here.

#base-file-for-exdends---------------------------
def  index_page(request:HttpRequest): 
    return render(request,"manager_app/manager.html")
#-------------------------------------


def category_page(request:HttpRequest):
    Catagorys=Catagory.objects.all()
    #for add new category
    if request.method=="POST":

        new_category=Catagory(name=request.POST["categoryname"])
        new_category.save()
        return redirect('manager_app:category_page')
    

    return render(request,"manager_app/category.html",{"Catagorys":Catagorys})




def delete_category(request:HttpRequest,category_id):
 
    category=Catagory.objects.get(id=category_id)
    category.delete()
    return redirect("manager_app:category_page")

#add_subcategory

def sub_category(request:HttpRequest,category_id):

    category=Catagory.objects.get(id=category_id)
    
    if request.method=="POST":
        new_subCategory=SubCatagory(category=category,name=request.POST["categoryname"])
        new_subCategory.save()

        return redirect('manager_app:sub_category',category_id)
    sub_category=SubCatagory.objects.filter(category=category)
    return render(request,"manager_app/sub_category_page.html" ,{"category":category, "sub_category":sub_category})




def delete_sub_category(request:HttpRequest,category_id,sub_category_id):
   
    sub_category=SubCatagory.objects.get(id=sub_category_id)
    sub_category.delete()
    return redirect('manager_app:sub_category',category_id)

def add_found_item_page(request:HttpRequest):
    catagorys=Catagory.objects.all()
    sub_category=SubCatagory.objects.all()


    return render(request,"manager_app/add_found_item_page.html",{"catagorys":catagorys,"sub_category":sub_category})
    



