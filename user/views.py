from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm
from user.models import UserRecord, ContactUs, userProfile
from user.forms import UserRecordForm, userProfileForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

#userhome handling
def userHome(request):
    response = redirect('/user/records')
    return response

#user profile page handling
def userProfilehandel(request):
    
    #handling get request
    if request.user.is_authenticated:
        bool = "true"
        userprofiles = userProfile.objects.filter(user=request.user).first()
        form = userProfileForm(instance=userprofiles)
        profile = {"form": form, 'bool': bool, 'userprofile': userprofiles}
    else:
        bool = "false"
        profile = {'bool': bool}

    #handling post request

    if request.user.is_authenticated and request.method == "POST":
        userprofile1 = userProfile.objects.filter(user=request.user).first()
        form = userProfileForm(request.POST, request.FILES, instance=userprofile1)
        if form.is_valid():
            userProfile1 = form.save(commit=False)
            userProfile1.user = request.user
            form.save()
            return redirect('/user/profile')
    return render(request, 'user/profile.html', profile)


#handling user's all records

def userRecords(request):
    
    if request.user.is_authenticated:
        recordsPending = UserRecord.objects.filter(user=request.user,status="pending")
        recordsRejected = UserRecord.objects.filter(user=request.user,status="rejected")
        recordsApproved = UserRecord.objects.filter(user=request.user,status="approved")
        bool = "true"
        form = UserRecordForm()
        Allrecords = {'recordsPending': recordsPending,'recordsRejected':recordsRejected,'recordsApproved':recordsApproved, 'bool': bool, 'form': form}
    else:
        bool = "false"
        Allrecords = {'records': "", 'bool': bool}

    #handlong post request on user record's page
    if request.method == "POST":
        form = UserRecordForm(request.POST, request.FILES)
        if form.is_valid():
            userRecord = form.save(commit=False)
            userRecord.user = request.user
            form.save()
            messages.info(request, 'You have added new record successfully. we will contact you soon!')
            return redirect('/user/records')
    return render(request, 'user/records.html', Allrecords)

# handel user login reuest

def userLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect("userRecords")
        else:
             messages.info(request, 'Username or password is invalid, Please check it once.!')
             return redirect("userRecords")

    else:
        return render(request, 'error404.html')


def userLogout(request):
    logout(request)
    return redirect('userRecords')


def userSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.info(request, 'your username should not be less than 10 characters')
            return redirect('userRecords')

        if (pass1 != pass2):
            messages.info(request, 'your password 1 and 2 are not matching. Please, correct it!')
            return redirect('userRecords')

        # chekc username is unique or not and Create new user
        try:
            user= User.objects.get(username=username)
            messages.info(request, 'Your username is not unique. try another one')
            return redirect('userRecords') 
        except User.DoesNotExist:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            login(request, myuser)
            messages.info(request, 'Welcome to farmapp! You have created your account successfully')
            return redirect('userRecords')      
    else:
        return render(request, 'error404.html')


def contactUs(request):
    if request.method == "POST":
        name = request.POST.get('txtName', '')
        email = request.POST.get('txtEmail', '')
        phone = request.POST.get('txtPhone', '')
        msg = request.POST.get('txtMsg', '')
        print(name, email, phone, msg)
        contact = ContactUs(name=name, email=email, phone=phone, desc=msg)
        contact.save()
        messages.info(request, 'We got your query. we will look at soon.')
        return redirect('contactus') 
    return render(request, 'user/contactus.html')
