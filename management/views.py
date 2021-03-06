from django.shortcuts import render,redirect
from user.models import UserRecord, ContactUs, userProfile,cropArea
from management.models import employee,crop,seedsModel,pesticidesModel
from django.contrib import messages
from management.forms import EmployeeForm,CropForm,SeedsForm,PesticidesFrom,addCropToRecord
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def home(request):
    return render(request, 'management/managementhome.html')

def manage(request):
    if request.POST.get("Approve"):
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Approve"))
        ToHandle.update(status="approved")
        

    elif request.POST.get("Reject"):  
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Reject"))
        ToHandle.update(status="rejected")
     
    
    
    
    recordsPending = UserRecord.objects.filter(status="pending").order_by('timestamp')
    recordsRejected = UserRecord.objects.filter(status="rejected").order_by('timestamp')
    recordsApproved = UserRecord.objects.filter(status="approved").order_by('timestamp')
    Allrecords = {'recordsPending': recordsPending,'recordsRejected':recordsRejected,'recordsApproved':recordsApproved}
    return render(request, 'management/manage.html',Allrecords)


def cropRecord(request):
    crp=[]
    if request.POST.get("AddNewCrop"):
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have added new crop record successfully.')
            return redirect('/management/crop/')

    elif request.POST.get("AddCropToRecord"):
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("AddCropToRecord")).first()
        form=addCropToRecord(request.POST,instance=ToHandle)
        if form.is_valid():
            
            
            #cheking croparea model has already crop added or not for particular user record.
            cropIs=cropArea.objects.filter(userRecord=ToHandle,crop=request.POST['selectCrop'])
            AreaIs=cropArea.objects.filter(userRecord=ToHandle)
            AreaIsLength=cropArea.objects.filter(userRecord=ToHandle).count()
            
            length=0
            TotalUsedArea=0
            for a in AreaIs:
                TotalUsedArea+=a.Area
            crparea = int(request.POST['croparea'])
           
            if ToHandle.farmArea< TotalUsedArea  + crparea:
                messages.info(request, 'You can add upto {} Acre area, please remove any crop or decrease area in any crop'.format(ToHandle.farmArea-TotalUsedArea) )
                
            else:
                ToHandle.selectCrop.add(request.POST['selectCrop'])
                if(cropIs):
                    cropIs[0].Area=request.POST['croparea']
                    cropIs[0].save()
                else:
                    ToaddCrop = crop.objects.filter(crop_id=request.POST['selectCrop'])[0]
                    NewcropArea = cropArea(userRecord=ToHandle,crop=ToaddCrop,Area=request.POST['croparea'])
                    NewcropArea.save()


                messages.info(request, 'You have updated crop successfully.')
            return redirect('/management/crop/')
        

    else:
        form = CropForm()
        addCropToRecordForm=addCropToRecord()
        
    cropRecord = crop.objects.all()
    recordsApproved = UserRecord.objects.filter(status="approved").order_by('timestamp')
    
    for recordNum in recordsApproved:
        ToHandle = cropArea.objects.filter(userRecord=recordNum)
        crp.append(ToHandle)
            
        
    dict = {'form': form,'addCrop':addCropToRecordForm,'cropRecord':cropRecord,'recordsApproved':recordsApproved,'crp':crp,'mylist' :zip(recordsApproved, crp)}
    return render(request, 'management/crop.html', dict)


def cropAllDetails(request,id):
    crop_id = crop.objects.filter(crop_id=id)
    seedsRecord = seedsModel.objects.filter(crop_name=crop_id[0].cropName)
    pesticidesRecord = pesticidesModel.objects.filter(crop_name=crop_id[0].cropName)

    if request.method == 'POST':
        form = SeedsForm(request.POST, request.FILES)
        if form.is_valid():
            seedsCrop = form.save(commit=False)
            seedsCrop.crop_name = crop_id[0].cropName
            form.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/crop/'+str(id))
    else:
        form = SeedsForm()

    if request.method == 'POST':
        form1 = PesticidesFrom(request.POST, request.FILES)
        if form1.is_valid():
            seedsCrop = form1.save(commit=False)
            seedsCrop.crop_name = crop_id[0].cropName
            form1.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/crop/' + str(id))
    else:
        form1 = PesticidesFrom()
        
        dict = {'form1':form1,'form':form,'cropId':crop_id[0],'seedsRecord':seedsRecord,'pesticidesRecord':pesticidesRecord}
    return render(request,'management/cropAllDetails.html',dict)


def cropRecords(request,id):

    if request.POST.get("RemoveCropToRecord"):
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("RemoveCropToRecord")).first()
        ToHandle.selectCrop.remove(id)
        
        cropArea.objects.filter(userRecord=ToHandle,crop=id).delete()
        
        messages.info(request, 'You have Removed crop successfully from record.')
        return redirect('/management/crop/cropRecords/'+str(id))
            

    crp=[]
    recordsInCrop = UserRecord.objects.filter(selectCrop=id).order_by('timestamp').order_by('timestamp')
    cropSelected = crop.objects.filter(crop_id=id)[0]
  
    for recordNum in recordsInCrop:
        crp.append(recordNum.selectCrop.all())
            
    dict = {'recordsInCrop':recordsInCrop,'crop':cropSelected,'mylist' :zip(recordsInCrop, crp)}
    return render(request,'management/cropRecords.html',dict)




def employeeRecords(request):
    employeeRecord = employee.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/employee/')
    else:
        form = EmployeeForm()
    dict = {'form': form, 'employeeRecord': employeeRecord}
    return render(request, 'management/employee.html', dict)

def employeeProfile(request,id):
    employeeId = employee.objects.filter(employee_id=id)
    return render(request,'management/employeeProfile.html',{'emid':employeeId[0]})


