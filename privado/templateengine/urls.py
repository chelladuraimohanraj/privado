from django.urls import path
 
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('te/customer/<customer_id>/templates',views.insert_retrive,name='insert_retrive'),
]
