from django.contrib import admin
from user.models import UserRecord,ContactUs,userProfile,cropArea

# Register your models here.
models = (UserRecord,ContactUs,userProfile,cropArea)
for m in models:
   admin.site.register(m)
