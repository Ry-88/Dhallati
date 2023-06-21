from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [

    path('', views.home, name='home'),
    path('not_found', views.not_found, name='not_found'),
    path('request/tracking/<track_id>', views.request_tracking, name='request_tracking'),
    path("category_for_add_request_add",views.category,name="category_for_add_request_add"),
    path('request_add/<category_id>/', views.request_add, name='request_add'),
    path("request_add/email/<track_id>/",views.email_page,name="email_page"),
    path('form/check/<confirm_item_id>/' ,views.email_check_form,name="email_check_form"),


    
]