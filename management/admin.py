from django.contrib import admin
from management.models import employee,crop,seedsModel,pesticidesModel

# Register your models here.

models = (employee,crop,seedsModel,pesticidesModel)
for m in models:
   admin.site.register(m)
