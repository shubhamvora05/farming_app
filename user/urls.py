from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("",views.userHome,name='userhome'),

    #account creation urls
    path("login",views.userLogin,name='userLogin'),
    path("logout",views.userLogout,name='userLogout'),
    path("signup",views.userSignup,name='userSignup'),
    

    path("records",views.userRecords,name='userRecords'),
    path("profile",views.userProfilehandel,name='userProfile'),
    path("contactus",views.contactUs,name='contactus'),
    path("AboutUs",views.AboutUs,name='AboutUs'),
    path("Pricing",views.Pricing,name='Pricing_plans'),
    
    #password reset urls
    path("reset_password/",auth_views.PasswordResetView.as_view(template_name="user/reset_password.html"), name="reset_password"),
    path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name="user/reset_password_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm" ),
    path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(template_name="user/reset_password_complete.html"),name="password_reset_complete"),
]
