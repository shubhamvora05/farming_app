from django import forms
from user.models import UserRecord,userProfile

class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ('name','mobileNo','farmaddress','farmArea','soilType','moneyDemand','farmImage','extraComment',)

class userProfileForm(forms.ModelForm):
    class Meta:
        model=userProfile
        fields=('mobileNo','ProfilePic',)