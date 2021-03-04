from django.contrib import admin
from management.models import employee,crop,seedsModel,pesticidesModel

# Register your models here.

admin.site.register(employee)
admin.site.register(crop)
admin.site.register(seedsModel)
admin.site.register(pesticidesModel)