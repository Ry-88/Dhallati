from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('not_found', views.not_found, name='not_found'),
    path('request_add', views.request_add, name='request_add'),
    path('request_detail', views.request_detail, name='request_detail'),
    path('request_tracking', views.request_tracking, name='request_tracking'),
    
]