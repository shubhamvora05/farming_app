from django import forms
from user.models import UserRecord

class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ('name','mobileNo','farmaddress','farmArea','soilType','moneyDemand','farmImage','extraComment',)

