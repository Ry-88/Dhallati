from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
" from main_app.models import Catagory,SubCatagory "


# Create your views here.

def  index_page(request:HttpRequest):
    Catagorys=Catagory.objects.all()
    return render(request,"manager_app/manager.html",{"Catagorys":Catagorys})


def add_category(request:HttpRequest):
    if request.method=="POST":
        new_category=Catagory(name=request.POST["categoryname"])
        new_category.save()
        return redirect('manager_app:add_subcategory')
    return render(request,"manager_app/add_category_page.html")




def add_subcategory(request:HttpRequest,category_id):

    category=Catagory.objects.get(id=category_id)
    if request.method=="POST":
        new_subCategory=Catagory(category=category,name=request.POST["categoryname"])
        new_subCategory.save()
        return redirect('manager_app:add_subcategory')
    return render(request,"manager_app/add_category_page.html")
