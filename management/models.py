from django.db import models

# Create your models here.
class crop(models.Model):
    crop_id=models.AutoField(primary_key=True)
    cropName=models.CharField(max_length=30, blank=False, null=False)
    cropType=models.CharField(max_length=10, blank=False, null=False)
    totalStorage=models.IntegerField(default=0)
    cropSeason=models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.cropName