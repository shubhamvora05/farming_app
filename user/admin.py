from django.contrib import admin
from user.models import UserRecord,ContactUs,userProfile

# Register your models here.
models = (UserRecord,ContactUs,userProfile)
for m in models:
   admin.site.register(m)
