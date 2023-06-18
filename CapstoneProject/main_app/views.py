from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import RequestLostItem, Catagory, SubCatagory,ContactForm
from django.core.mail import send_mail, BadHeaderError
#from .forms import ContactForm


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
    """     if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(first_name,last_name, message, from_email, ["DhallatiOfficial@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "main_app/home.html", {"form": form})
"""
    try:
            
            if request.method == 'POST':

                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                message = request.POST.get('message')

                # Save contact data to the database
                contact = ContactForm(first_name=first_name, last_name=last_name , email=email, message=message)
                contact.save()

                # Retrieve all contacts
                contacts = ContactForm.objects.all()
                print(contact.email,contact.first_name,contact.last_name,contact.message)
                # Send email
                subject = f"subject {contact.first_name}"
                print("dsfds")
                send_mail(subject, contact.message, 'DhallatiOfficial@gmail.com' , ['DhallatiOfficial@gmail.com'],fail_silently=False)
               
                # Render success page or redirect
                return render(request, 'main_app/success.html')

            return render(request, 'main_app/home.html')
    except Exception as e:
                print(e)
                return render(request,"main_app/home.html")
    
def successView(request):
    return HttpResponse("Success! Thank you for your message.") 


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


    

def request_detail(request: HttpRequest):

    return render(request, 'main_app/request_detail.html')


def request_tracking(request: HttpRequest):

    return render(request, 'main_app/request_tracking.html')
