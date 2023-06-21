from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main_app.models import Catagory,SubCatagory,FoundItem,RequestLostItem,ConfirmItem
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.

#base-file-for-exdends---------------------------
@login_required(login_url="/accounts/log_in")
def  index_page(request:HttpRequest): 
    found_items =FoundItem.objects.all()
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,"manager_app/manager.html" ,{"found_items":found_items,"bell":bell})
#-------------------------------------




#--------------category -- views-------------------------------------------------------------------------------------------
@login_required(login_url="/accounts/log_in")
def category_page(request:HttpRequest):
    Catagorys=Catagory.objects.all()
    #for add new category
    if request.method=="POST":

        new_category=Catagory(name=request.POST["categoryname"])
        new_category.save()
        return redirect('manager_app:category_page')
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,"manager_app/category.html",{"Catagorys":Catagorys,"bell":bell})



@login_required(login_url="/accounts/log_in")
def delete_category(request:HttpRequest,category_id):
 
    category=Catagory.objects.get(id=category_id)
    category.delete()
    return redirect("manager_app:category_page")

#add_subcategory
@login_required(login_url="/accounts/log_in")
def sub_category(request:HttpRequest,category_id):

    category=Catagory.objects.get(id=category_id)
    
    if request.method=="POST":
        new_subCategory=SubCatagory(category=category,name=request.POST["categoryname"])
        new_subCategory.save()

        return redirect('manager_app:sub_category',category_id)
    sub_category=SubCatagory.objects.filter(category=category)
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,"manager_app/sub_category_page.html" ,{"category":category, "sub_category":sub_category,"bell":bell})


@login_required(login_url="/accounts/log_in")
def delete_sub_category(request:HttpRequest,category_id,sub_category_id):
   
    sub_category=SubCatagory.objects.get(id=sub_category_id)
    sub_category.delete()
    return redirect('manager_app:sub_category',category_id)

#---------------end-category--------------------------------------------------------------------------------------------------------------




# if the the manager want to add found item , frist well choose category then will go to 'add_found_item_page'
@login_required(login_url="/accounts/log_in")
def category_for_add_found(request:HttpRequest):
    catagorys = Catagory.objects.all()
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,'manager_app/category_for_add_fuond.html',{"catagorys":catagorys,"bell":bell})


@login_required(login_url="/accounts/log_in")
def add_found_item_page(request:HttpRequest ,category_id):
    catagory=Catagory.objects.get(id=category_id)
    sub_category=SubCatagory.objects.filter(category=catagory)
    if request.method=="POST":
        new_found_item=FoundItem(catagory=catagory,Sub_catagory= SubCatagory.objects.get(id=request.POST["sub_category"]) ,color=request.POST["color"],place=request.POST["place"],description=request.POST["description"],image=request.FILES["image"])
        new_found_item.save()
        return redirect("manager_app:found_item_page")
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,"manager_app/add_found_item_page.html",{"catagory":catagory,"sub_category":sub_category,"bell":bell})
















#----------------------------------------------------------------
@login_required(login_url="/accounts/log_in")
def found_item_page(request:HttpRequest):

    catagory = Catagory.objects.all()
    if not request.user.is_staff:
        return redirect("main_app:not_found")
    

    found_items =FoundItem.objects.filter(status = "T")
    bell =RequestLostItem.objects.filter(is_read=False)

    if "search" in request.GET:
        search_word=request.GET["search"]
        found_items=FoundItem.objects.filter(description__contains=search_word,status = "T")
    if "category"in request.GET:
        category=request.GET["category"]
        found_items=FoundItem.objects.filter(catagory__name=category, status="T")
    
    return render(request,"manager_app/found_items.html",{"found_items":found_items,"bell":bell, "catagory":catagory})



@login_required(login_url="/accounts/log_in")
def delete_found_item(request:HttpRequest,found_item_id):
    found_item=FoundItem.objects.get(id=found_item_id)
    found_item.delete()
    redirect("manager_app:found_item_page")



def found_detail_page(request:HttpRequest,found_item_id):
    
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.filter(catagory=found_item.catagory,Sub_catagory=found_item.Sub_catagory,status="T")
    confirm_items=ConfirmItem.objects.filter(found_item=found_item)
  
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,'manager_app/founditem_detail.html' ,{"found_item":found_item,"request_lost_Items":lost_item,"confirm_items":confirm_items,"bell":bell })


@login_required(login_url="/accounts/log_in")
def confirm_item_for_found_detail(request:HttpRequest,found_item_id,request_lost_item_id):
 

   found_item=FoundItem.objects.get(id=found_item_id)
   lost_item=RequestLostItem.objects.get(id=request_lost_item_id)
   new_confirm =ConfirmItem(found_item=found_item,request_Lost_Item=lost_item)
   new_confirm.save()
   found_item.status="M"
   lost_item.status="M"
   found_item.save()
   lost_item.save()   
   

    

   return redirect("manager_app:lost_item_detail_page",request_lost_item_id)




#-------------------------------------------------------------------

@login_required(login_url="/accounts/log_in")
def lost_item_page(request:HttpRequest):
    request_lost_Items=RequestLostItem.objects.filter(status = "T").order_by("is_read","-created_at")
    catagory=Catagory.objects.all()
    if "search" in request.GET:
        search_word=request.GET["search"]
        request_lost_Items=RequestLostItem.objects.filter(description__contains=search_word)
    if "category"in request.GET:
        category=request.GET["category"]
        request_lost_Items=RequestLostItem.objects.filter(catagory__name=category, status="T")
  
    return render(request,'manager_app/lost_item_request_page.html' ,{"request_lost_Items":request_lost_Items,"catagory":catagory})

@login_required(login_url="/accounts/log_in")
def delete_lost_item(request:HttpRequest,lost_item_id):
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    lost_item.delete()
    return redirect("manager_app:lost_item_page")

@login_required(login_url="/accounts/log_in")
def lost_item_detail_page(request:HttpRequest,lost_item_id):
    
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    found_item=FoundItem.objects.filter(catagory=lost_item.catagory,Sub_catagory=lost_item.Sub_catagory,status="T")
    lost_item.is_read=True
    lost_item.save()
    confirm_items=ConfirmItem.objects.filter(request_Lost_Item=lost_item)
    bell =RequestLostItem.objects.filter(is_read=False)
    return render(request,'manager_app/lost_item_request_detail.html' ,{"found_item":found_item,"lost_item":lost_item,"confirm_items":confirm_items,"bell":bell })




# button to add confirm_item for request
@login_required(login_url="/accounts/log_in")
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


# button to change 'is_confirm'==True  request and send email the item  is for him
@login_required(login_url="/accounts/log_in")
def confirm_item_true_for_lost_detail(request:HttpRequest,found_item_id,lost_item_id):
    
    found_item=FoundItem.objects.get(id=found_item_id)
    lost_item=RequestLostItem.objects.get(id=lost_item_id)
    confirm_item=ConfirmItem.objects.get(found_item=found_item)
    if not confirm_item.is_confirm==True:
        confirm_item.is_confirm=True
        found_item.status="F"
        lost_item.status="F"

       
    
        subject=f"confirm the item"
        content=f"Hello {confirm_item.request_Lost_Item.name} \n\
        we found you item please vist us to claim your {confirm_item.request_Lost_Item.Sub_catagory.name} {confirm_item.request_Lost_Item.catagory.name} \n\
             thank you for trusting us"
        send_mail(subject, content, 'DhallatiOfficial@gmail.com' , [confirm_item.request_Lost_Item.email],fail_silently=False)
        found_item.save()
        lost_item.save()
        return redirect("manager_app:confirm_item_page")
    else :
        found_item.status="M"
        lost_item.status="M"
        confirm_item.is_confirm=False
    confirm_item.save()
    return redirect("manager_app:lost_item_detail_page",lost_item_id)



# button to delete  request
@login_required(login_url="/accounts/log_in")
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



@login_required(login_url="/accounts/log_in")
def confirm_item_page(request:HttpRequest):
    catagory=Catagory.objects.all()
    confirmed_items = ConfirmItem.objects.filter(is_confirm = True)
    bell =RequestLostItem.objects.filter(is_read=False)
    if "search" in request.GET:
        search_word=request.GET["search"]
        confirmed_items=ConfirmItem.objects.filter(found_item__description__contains=search_word, is_confirm = True)
    if "category"in request.GET:
        category=request.GET["category"]
        confirmed_items=ConfirmItem.objects.filter(found_item__catagory__name=category, is_confirm = True)
    return render(request,'manager_app/confirm_item_page.html', {"confirmed_items" : confirmed_items,"bell":bell,"catagory":catagory })

  
@login_required(login_url="/accounts/log_in")
def match_item_page(request:HttpRequest):
    catagory=Catagory.objects.all()
    matched_items = ConfirmItem.objects.filter(is_confirm = False)
    bell =RequestLostItem.objects.filter(is_read=False)
    if "search" in request.GET:
        search_word=request.GET["search"]
        matched_items=ConfirmItem.objects.filter(found_item__description__contains=search_word, is_confirm = False)
    if "category"in request.GET:
        category=request.GET["category"]
        matched_items=ConfirmItem.objects.filter(found_item__catagory__name=category, is_confirm = False)
    return render(request, "manager_app/match_item_page.html", {"matched_items" : matched_items,"bell":bell,"catagory":catagory})


@login_required(login_url="/accounts/log_in")
def send_email_form(request:HttpRequest,lost_item_id,confirm_item_id):

    
    confirm_item=ConfirmItem.objects.get(id=confirm_item_id)
    if not confirm_item.is_send:
        confirm_item.is_send=True
        subject=f"Hello {confirm_item.request_Lost_Item.name}"
        content=f"Hello {confirm_item.request_Lost_Item.name} \n\
Regarding your request please answer these follow up questions to be sure \n\
http://127.0.0.1:8000/form/check/{confirm_item.id}"
        send_mail(subject, content, 'DhallatiOfficial@gmail.com' , [confirm_item.request_Lost_Item.email],fail_silently=False)
        confirm_item.save()
    else:
        confirm_item.is_send=False
        confirm_item.save()
    return redirect("manager_app:lost_item_detail_page",lost_item_id)



    


