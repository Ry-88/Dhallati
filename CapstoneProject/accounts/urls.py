from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('no_permission', views.no_permission, name='no_permission')
]