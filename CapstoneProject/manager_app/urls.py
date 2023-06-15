from django.urls import path
from . import views

app_name = "manager_app"

urlpatterns = [
    path('',views.index_page,name="index_page"),

    path('add/category/',views.add_category,name="add_category"),
    path('add/category/<category_id>/subcategory',views.add_subcategory,name="add_subcategory")
    
]