from django.db import models
from django.contrib.auth.models  import User
from django.utils.timezone import now



# user record model
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Change_photo=models.ImageField(upload_to='user/profile_pic/',default="user/Profile_pic/default-user.png")

    def __str__(self):
        return self.user.username

class UserRecord(models.Model):

    sandySoil = "Sandy soil"
    siltSoil = "Silt Soil"
    claySoil= "Clay Soil"
    loamySoil="Loamy Soil"
    SOIL_CHOICES = (
    (sandySoil, "Sandy Soil"),
    (siltSoil, "Silt Soil"),
    (claySoil, "Clay Soil"),
    (loamySoil, "Loamy Soil"),
    )

    recordId=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length = 30, blank = False,null = False)
    mobileNo=models.CharField(max_length = 30, blank = False,null = False)
    farmaddress=models.CharField(max_length = 150, blank = False,null = False)
    farmArea=models.IntegerField(default=0)
    soilType=models.CharField(max_length = 11, choices = SOIL_CHOICES, default = siltSoil )
    moneyDemand=models.IntegerField(default=0)
    farmImage=models.ImageField(upload_to='user/farm/',default="")
    extraComment=models.TextField()
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.name

#contact us model
class ContactUs(models.Model):
    msg_id = models.AutoField(primary_key="true")
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.name