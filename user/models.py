from django.db import models
from django.contrib.auth.models  import User
from django.utils.timezone import now



# Create your models here.
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