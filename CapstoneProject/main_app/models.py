from django.db import models

# Create your models here.

class Catagory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.name}"


class SubCatagory(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, default="Other")
    def __str__(self) -> str:
        return f"{self.name}"



class RequestLostItem(models.Model):
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Sub_catagory=models.ForeignKey(SubCatagory, on_delete=models.CASCADE )
    COLOR_CHOICES=[
        ("R","Red"),
        ("G","Green"),
        ("B","Blue"),
        ("BLA","Black"),
        ("Y","Yellow"),
        ("W","White"),
    ]
    PLACE_CHOICES=[
        ("F","Frist Floor"),
        ("S","Secound Floor"),
        ("T","Third Floor"),
    ]
    STATUS_CHICES=[
        ("T","TRAKING"),
        ("M","MATCHED"),
        ("F","FOUND"),
        ("N","NOMATCH")
    ]


    color=models.CharField(max_length=100,choices=COLOR_CHOICES,default="B")
    place=models.CharField(max_length=100,choices=PLACE_CHOICES)
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    created_at=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS_CHICES,default="T")
    is_read=models.BooleanField(default=False)
    email=models.EmailField(default=' ')
    name=models.CharField(max_length=200, default=' ')
    phone_number=models.CharField(max_length=13, default=' ')




class FoundItem(models.Model):
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Sub_catagory=models.ForeignKey(SubCatagory, on_delete=models.CASCADE)

    COLOR_CHOICES=[
        ("R","Red"),
        ("G","Green"),
        ("B","Blue"),
        ("BLA","Black"),
        ("Y","Yellow"),
        ("W","White"),
    ]
    PLACE_CHOICES=[
        ("F","Frist Floor"),
        ("S","Secound Floor"),
        ("T","Third Floor"),
    ]
    STATUS_CHICES=[
        ("T","TRAKING"),
        ("M","MATCHED"),
        ("F","FOUND"),
        ("N","NOMATCH")
    ]
    color=models.CharField(max_length=100,choices=COLOR_CHOICES,default="B")
    place=models.CharField(max_length=100,choices=PLACE_CHOICES,default="T")
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    created_at=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS_CHICES,default="T")




class ConfirmItem(models.Model):
    found_item=models.OneToOneField(FoundItem,on_delete=models.CASCADE)
    request_Lost_Item=models.OneToOneField(RequestLostItem,on_delete=models.CASCADE)
    is_confirm=models.BooleanField(default=False)
    is_send=models.BooleanField(default=False) 
    is_reserved=models.BooleanField(default=False)
    message_form=models.TextField(default=" ")
    from_ai=models.BooleanField(default=False)
class ContactForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()



    

