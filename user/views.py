from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from user.models import UserRecord
from django.http import HttpResponse

# Create your views here.
def userHome(request):
    return render(request,'user/home.html')

def userRecords(request):
    if request.user.is_authenticated:
        records= UserRecord.objects.filter(user=request.user)
        bool="true"
        Allrecords={'records':records,'bool':bool} 
    else :
        bool="false"
        Allrecords={'records':"",'bool':bool}
    

    if request.method == "POST":
        user=request.user
        name=request.POST.get('fname')
        phone=request.POST.get('phone')
        farmAdress=request.POST.get('faddress')
        farmArea=request.POST.get('farea')
        soilType=request.POST.get('soilType')
        money=request.POST.get('money')
        farmImage=request.POST.get('farmImage')
        extraComment=request.POST.get('extracomment')
        userRecord=UserRecord(user=user, name=name, mobileNo=phone,farmaddress=farmAdress,farmArea=farmArea, soilType=soilType, moneyDemand=money,farmImage=farmImage, extraComment=extraComment)
        userRecord.save()
    return render(request,'user/records.html',Allrecords)

def userLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("userRecords")
        else:
           
            return redirect("userHome")

    return HttpResponse("404- Not found")


def userLogout(request):
    logout(request)
    return redirect('userHome')


def userSignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        #here, we need to send some error message to the user 
        if len(username)<10:
            return redirect('userHome')

        if not username.isalnum():
            return redirect('userHome')

        if (pass1!= pass2):
             return redirect('userHome')


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('userRecords')

    else:
        return HttpResponse("404 - Not found")
