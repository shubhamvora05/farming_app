from django.db import models
from django.utils.timezone import now


# Create your models here.
class crop(models.Model):

    monsoon = "Monsoon(Kharif Crop)"
    winter = "Winter(Rabi Crop)"
    summer ="Summer(Zaid Crop)"
    SEASON_CHOICES = (
        (monsoon, "Monsoon(Kharif Crop)"),
        (winter, "Winter(Rabi Crop)"),
        (summer, "Summer(Zaid Crop)"),
    )

    food = "FoodCrop(Grains)"
    fruits = "Fruits"
    veg = "Vegetables"
    NonFood = "Non FoodCrop"
    TYPE_CHOICES = (
        (food, "FoodCrop(Grains)"),
        (fruits, "Fruits"),
        (veg, "Vegetables"),
        (NonFood, "Non FoodCrop"),
    )


    crop_id=models.AutoField(primary_key=True)
    cropName=models.CharField(max_length=30, blank=False, null=False)
    cropType = models.CharField(max_length=40, choices=TYPE_CHOICES, default=food)
    totalStorage=models.IntegerField(default=0)
    cropSeason = models.CharField(max_length=40, choices=SEASON_CHOICES, default=monsoon)

    def __str__(self):
        return self.cropName

#employee model
class employee(models.Model):

    crop = "Crop Department"
    seeds = "Seeds Department"
    workers = "Workers Department"
    DEPARTMENT_CHOICES = (
        (crop, "Crop Department"),
        (seeds, "Seeds Department"),
        (workers, "Workers Department"),
    )

    employee_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, blank=False, null=False)
    mobileNo = models.CharField(max_length=10, blank=False, null=False)
    age=models.IntegerField(default=0)
    departmentType = models.CharField(max_length=40, choices=DEPARTMENT_CHOICES, default=crop)
    profileImage = models.ImageField(upload_to='management/employeeProfile/', default="")
    address = models.CharField(max_length=150, blank=False, null=False)
    ability =  models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class seedsModel(models.Model):
    seeds_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=30, blank=False, null=False)
    seeds_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.seeds_name

class pesticidesModel(models.Model):
    pesticides_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=30, blank=False, null=False)
    pesticides_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.pesticides_name

