from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),

    path('signup/',signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

    path('',product_list,name='products'),


    path('add/<int:product_id>/',add_cart,name='add_cart'),
    path('cart/',cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',cart_remove,name='cart_remove'),

    
    path('full_remove/<int:product_id>/',full_remove,name='full_remove'),
    path('place-order/', place_order, name='place_order'),


     

    ]


    
    

