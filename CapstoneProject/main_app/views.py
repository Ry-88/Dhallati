from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import RequestLostItem, Catagory, SubCatagory, ContactForm
from django.core.mail import send_mail, BadHeaderError
# from .forms import ContactForm


# Create your views here.


def home(request: HttpRequest):
    
    msg=" "

    if request.method == 'POST':

        if 'track' in request.POST:
            track_request= RequestLostItem.objects.get(id=request.POST['request_number'])
            return redirect("main_app:request_tracking",track_request.id)

            

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


    return render(request, 'main_app/home.html', {"msg": msg})



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

        new_request = RequestLostItem(catagory=category, Sub_catagory=SubCatagory.objects.get(id=request.POST["sub_category"]), color=request.POST["color"],

                                      place=request.POST["place"], description=request.POST["description"],
                                      email=request.POST["email"],
                                      name=request.POST["name"],
                                      phone_number=request.POST["phone_number"])

        new_request.save()
        return redirect("main_app:home")

    return render(request, 'main_app/request_add.html', {"category": category, "sub_category": sub_category})


#def request_detail(request: HttpRequest, lost_id):

#    requests = RequestLostItem.objects.get(id=lost_id)

#    return render(request, 'main_app/request_detail.html', {'requests': requests})



def request_tracking(request: HttpRequest, track_id):

    tracking = RequestLostItem.objects.get(id=track_id)

    
    return render(request, 'main_app/request_tracking.html', {'tracking' : tracking})

