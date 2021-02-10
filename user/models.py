from django.db import models
from django.contrib.auth.models  import User
from django.utils.timezone import now


# Create your models here.
class UserRecord(models.Model):
    userId=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, default="")
    mobileNo=models.CharField(max_length=12,default="")
    farmaddress=models.TextField(default="")
    farmArea=models.IntegerField(default=0)
    soilType=models.TextField(default="")
    moneyDemand=models.IntegerField(default=0)
    farmImage=models.ImageField(upload_to='user/farm',default="")
    extraComment=models.TextField()
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.name