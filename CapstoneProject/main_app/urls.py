from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [

    path('', views.home, name='home'),
    path('not_found', views.not_found, name='not_found'),
    path('request_detail', views.request_detail, name='request_detail'),
    path('request_tracking', views.request_tracking, name='request_tracking'),
    path("category_for_add_request_add",views.category,name="category_for_add_request_add"),
    path('request_add/<category_id>/', views.request_add, name='request_add'),

    
]