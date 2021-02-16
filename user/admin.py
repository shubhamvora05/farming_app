from django.contrib import admin
from user.models import UserRecord,ContactUs,UserProfile

# Register your models here.
models = (UserRecord,ContactUs,UserProfile)
for m in models:
   admin.site.register(m)
