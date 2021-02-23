from django.shortcuts import render
from user.models import UserRecord, ContactUs, userProfile

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'management/base.html')

def manage(request):
    if request.POST.get("Approve"):
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Approve"))
        ToHandle.update(status="approved")
        

    elif request.POST.get("Reject"):  
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Reject"))
        ToHandle.update(status="rejected")
     
    
    
    
    recordsPending = UserRecord.objects.filter(status="pending")
    recordsRejected = UserRecord.objects.filter(status="rejected")
    recordsApproved = UserRecord.objects.filter(status="approved")
    Allrecords = {'recordsPending': recordsPending,'recordsRejected':recordsRejected,'recordsApproved':recordsApproved}
    return render(request, 'management/manage.html',Allrecords)

def crop(request):
    return render(request, 'management/base.html')

def seeds(request):
    return render(request, 'management/base.html')

def finance(request):
    return render(request, 'management/base.html')

def employee(request):
    return render(request, 'management/base.html')