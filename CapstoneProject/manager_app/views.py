from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main_app.models import Catagory,SubCatagory,FoundItem,RequestLostItem,ConfirmItem

from django.core import serializers
import json

# Create your views here.

#base-file-for-exdends---------------------------
def  index_page(request:HttpRequest): 
    found_items =FoundItem.objects.all()


    
    return render(request,"manager_app/manager.html" ,{"found_items":found_items})
#-------------------------------------




#--------------category -- views-------------------------------------------------------------------------------------------
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

#---------------end-category--------------------------------------------------------------------------------------------------------------




# if the the manager want to add found item , frist well choose category then will go to 'add_found_item_page'
def category_for_add_found(request:HttpRequest):
    catagorys = Catagory.objects.all()
    return render(request,'manager_app/category_for_add_fuond.html',{"catagorys":catagorys})


def add_found_item_page(request:HttpRequest ,category_id):
    catagory=Catagory.objects.get(id=category_id)
    sub_category=SubCatagory.objects.filter(category=catagory)
    if request.method=="POST":
        new_found_item=FoundItem(catagory=catagory,Sub_catagory= SubCatagory.objects.get(id=request.POST["sub_category"]) ,color=request.POST["color"],place=request.POST["place"],description=request.POST["description"],image=request.FILES["image"])
        new_found_item.save()
        return redirect("manager_app:index_page")
    return render(request,"manager_app/add_found_item_page.html",{"catagory":catagory,"sub_category":sub_category})
















#----------------------------------------------------------------

def found_item_page(request:HttpRequest):
    found_items =FoundItem.objects.all()
    return render(request,"manager_app/found_items.html",{"found_items":found_items})



def found_detail_page(request:HttpRequest,found_item_id):
    
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.filter(catagory=found_item.catagory,Sub_catagory=found_item.Sub_catagory,status="T")
    confirm_items=ConfirmItem.objects.filter(found_item=found_item)
  

    return render(request,'manager_app/founditem_detail.html' ,{"found_item":found_item,"request_lost_Items":lost_item,"confirm_items":confirm_items })



def confirm_item_for_found_detail(request:HttpRequest,found_item_id,request_lost_item_id):
 

   found_item=FoundItem.objects.get(id=found_item_id)
   lost_item=RequestLostItem.objects.get(id=request_lost_item_id)
   new_confirm =ConfirmItem(found_item=found_item,request_Lost_Item=lost_item)
   new_confirm.save()
   found_item.status="M"
   lost_item.status="M"
   found_item.save()
   lost_item.save()   
   

    

   return redirect("manager_app:found_detail_page",found_item_id)



def discard_confirm_item_for_found_detail(request:HttpRequest,found_item_id,request_lost_item_id):
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=request_lost_item_id)
    found_item.status="T"
    lost_item.status="T"
    found_item.save()
    lost_item.save()
    confirm_item=ConfirmItem.objects.get(found_item=found_item)
    
    confirm_item.delete()

    return redirect("manager_app:found_detail_page",found_item_id)

def confirm_item_true_for_found_detail(request:HttpRequest,found_item_id,request_lost_item_id):
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=request_lost_item_id)
    confirm_item=ConfirmItem.objects.get(found_item=found_item)
    confirm_item.is_confirm=True
    confirm_item.save()
    found_item.status="F"
    lost_item.status="F"
    found_item.save()
    lost_item.save()
   

    return redirect("manager_app:found_detail_page",found_item_id)
















#-------------------------------------------------------------------


def lost_item_page(request:HttpRequest):
    request_lost_Items=RequestLostItem.objects.filter()

    return render(request,'manager_app/lost_item_request_page.html' ,{"request_lost_Items":request_lost_Items})

def lost_item_detail_page(request:HttpRequest,lost_item_id):
    
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    found_item=FoundItem.objects.filter(catagory=lost_item.catagory,Sub_catagory=lost_item.Sub_catagory,status="T")
    confirm_items=ConfirmItem.objects.filter(request_Lost_Item=lost_item)
    return render(request,'manager_app/lost_item_request_detail.html' ,{"found_item":found_item,"lost_item":lost_item,"confirm_items":confirm_items })




# button to add confirm_item for request
def confirm_item_for_lost_detail(request:HttpRequest,found_item_id,lost_item_id):
   

    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    new_confirm =ConfirmItem(found_item=found_item,request_Lost_Item=lost_item)
    new_confirm.save()
    found_item.status="M"
    lost_item.status="M"
    found_item.save()
    lost_item.save()
 
    return redirect("manager_app:lost_item_detail_page",lost_item_id)


# button to change 'is_confirm'==True  request
def confirm_item_true_for_lost_detail(request:HttpRequest,found_item_id,lost_item_id):
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    found_item.status="F"
    lost_item.status="F"
    found_item.save()
    lost_item.save()
    confirm_item=ConfirmItem.objects.get(found_item=found_item)
    confirm_item.is_confirm=True
    confirm_item.save()

    return redirect("manager_app:lost_item_detail_page",lost_item_id)



# button to delete  request
def discard_confirm_item_for_lost_detail(request:HttpRequest,found_item_id,lost_item_id):
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    found_item.status="T"
    lost_item.status="T"
    found_item.save()
    lost_item.save()
    confirm_item=ConfirmItem.objects.get(found_item=found_item)
    
    confirm_item.delete()

    return redirect("manager_app:lost_item_detail_page",lost_item_id)



def confirm_item_page(request:HttpRequest):


    
    return render(request,'manager_app/confirm_item_page.html')