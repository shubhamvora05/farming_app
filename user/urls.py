from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.userHome,name='userHome'),
    path("login",views.userLogin,name='userLogin'),
    path("signup",views.userSignup,name='userSignup'),
    path("records",views.userRecords,name='userRecords'),
]
