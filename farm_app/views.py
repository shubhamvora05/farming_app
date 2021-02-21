from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"home.html")

def aboutUs(request):
    return render(request,"aboutUs.html")

def errorHandler(request):
    return render(request,"error404.html")