from django.contrib import admin
from .models import RequestLostItem, Catagory,SubCatagory

# Register your models here.


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Catagory, CatagoryAdmin)

class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')
admin.site.register(SubCatagory, SubCatagoryAdmin)


class RequestLostItemAdmin(admin.ModelAdmin):
    list_display = ('catagory','Sub_catagory','color', 'place', 'description', 'created_at')
admin.site.register(RequestLostItem, RequestLostItemAdmin)
