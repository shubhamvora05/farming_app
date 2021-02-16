from django import forms
from user.models import UserRecord,UserProfile

class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ('name','mobileNo','farmaddress','farmArea','soilType','moneyDemand','farmImage','extraComment',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('Change_photo',)