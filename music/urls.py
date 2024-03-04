from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('logout',logout,name='logout'),

    
]
