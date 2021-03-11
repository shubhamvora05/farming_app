from django import forms
from management.models import employee,crop,seedsModel,pesticidesModel
from user.models import UserRecord

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('name','mobileNo','age','departmentType','profileImage','address','ability',)

class CropForm(forms.ModelForm):
    class Meta:
        model = crop
        fields = ('cropName','cropType','cropSeason','totalStorage',)

class addCropToRecord(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ('selectCrop',)

class SeedsForm(forms.ModelForm):
    class Meta:
        model = seedsModel
        fields = ('seeds_name',)

class PesticidesFrom(forms.ModelForm):
    class Meta:
        model = pesticidesModel
        fields = ('pesticides_name',)