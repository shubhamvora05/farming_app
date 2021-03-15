from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='managementHome'),
    path("manage",views.manage,name='managementDepartment'),
    path("finance",views.finance,name='financeDepartment'),
    

    path("crop/",views.cropRecord,name='CropDepartment'),
    path("employee/",views.employeeRecords,name='employee'),
    path("employee/<int:id>", views.employeeProfile, name='employeeProfile'),
    path("crop/<int:id>", views.cropAllDetails, name='corpdetails'),
    path("crop/cropRecords/<int:id>", views.cropRecords, name='cropRecords'),
]
