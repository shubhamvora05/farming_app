from django import forms
from management.models import employee,crop,seedsModel,pesticidesModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('name','mobileNo','age','departmentType','profileImage','address','ability',)

class CropForm(forms.ModelForm):
    class Meta:
        model = crop
        fields = ('cropName','cropType','cropSeason','totalStorage',)

class SeedsForm(forms.ModelForm):
    class Meta:
        model = seedsModel
        fields = ('seeds_name',)

class PesticidesFrom(forms.ModelForm):
    class Meta:
        model = pesticidesModel
        fields = ('pesticides_name',)