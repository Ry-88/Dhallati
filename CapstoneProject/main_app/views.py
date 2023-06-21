from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import RequestLostItem, Catagory, SubCatagory, ContactForm,ConfirmItem
from django.core.mail import send_mail, BadHeaderError
import time
# from .forms import ContactForm


# Create your views here.


def home(request: HttpRequest):
    msg2=None
    msg=None

    if request.method == 'POST':

        if 'track' in request.POST:
            try:
                track_request= RequestLostItem.objects.get(id=request.POST['request_number'])
                return redirect("main_app:request_tracking",track_request.id)
            except:
                return redirect("/?msg=true#contactus")


        if 'help' in request.POST:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                message = request.POST.get('message')

                # Save contact data to the database
                contact = ContactForm(first_name=first_name,
                                      last_name=last_name, email=email, message=message)
                contact.save()

                # Retrieve all contacts
                contacts = ContactForm.objects.all()
                print(contact.email, contact.first_name,
                      contact.last_name, contact.message)
                # Send email
                subject = f"Hello my name is {contact.first_name}"
                content = f"Name: {contact.first_name} {contact.last_name} Email: {contact.email} Messege:{contact.message}"
                send_mail(subject, content, 'DhallatiOfficial@gmail.com',
                          ['DhallatiOfficial@gmail.com'], fail_silently=False)
                msg = "thank you for the feedback"
                # Render success page or redirect


    return render(request, 'main_app/home.html', {"msg": msg, "msg2":msg2})


def not_found(request: HttpRequest):

    return render(request, 'main_app/not_found.html')


def category(request: HttpRequest):
    categories = Catagory.objects.all()
    return render(request, 'main_app/category_for_add_request_add.html', {"categories": categories})


def request_add(request: HttpRequest, category_id):

    category = Catagory.objects.get(id=category_id)
    sub_category = SubCatagory.objects.filter(category=category)

    if request.method == "POST":

        if "image" in request.FILES:
            new_request = RequestLostItem(catagory=category, Sub_catagory=SubCatagory.objects.get(id=request.POST["sub_category"]), color=request.POST["color"],
                                          place=request.POST["place"], description=request.POST["description"],
                                          image=request.FILES["image"],
                                          email=request.POST["email"],
                                          name=request.POST["name"],
                                          phone_number=request.POST["phone_number"])

        else: new_request = RequestLostItem(catagory=category, Sub_catagory=SubCatagory.objects.get(id=request.POST["sub_category"]), color=request.POST["color"],

                                      place=request.POST["place"], description=request.POST["description"],
                                      email=request.POST["email"],
                                      name=request.POST["name"],
                                      phone_number=request.POST["phone_number"])

        new_request.save()
        name= request.POST["name"]
        email= request.POST["email"]
        
        track_number =new_request.id
        subject=f"your request "
        content=f"Hello {name} \n\
        Regarding your request  \n\
        your track number is # {track_number} \n\
        or <a href=' http://127.0.0.1:8000/request/tracking/{track_number}'> click hare view your track</a>"
        send_mail(subject, content, 'DhallatiOfficial@gmail.com' , [email] ,fail_silently=False,html_message=content)

        
        return redirect("main_app:email_page",new_request.id)

    return render(request, 'main_app/request_add.html', {"category": category, "sub_category": sub_category})


def email_page(request:HttpRequest, track_id):

    track_id = RequestLostItem.objects.get(id=track_id)
    
    return render(request,'main_app/email_page.html', {"track_id":track_id})



def request_tracking(request: HttpRequest, track_id):

    tracking = RequestLostItem.objects.get(id=track_id)

    
    return render(request, 'main_app/request_tracking.html', {'tracking' : tracking})

def email_check_form(request: HttpRequest,confirm_item_id):
    msg=None
    confirm_item=None
    try:
        confirm_item=ConfirmItem.objects.get(id=confirm_item_id)
        if request.method=="POST":
            confirm_item.message_form=request.POST["message_form"]
            confirm_item.is_reserved=True
            confirm_item.save()
            return redirect("main_app:home")
    except:
        msg="you enter wrong form"

    return render(request,"main_app/check_email_form.html",{"confirm_item":confirm_item ,"msg":msg})
        
