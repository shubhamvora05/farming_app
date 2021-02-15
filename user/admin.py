from django.contrib import admin
from user.models import UserRecord,ContactUs

# Register your models here.
models = (UserRecord,ContactUs)
for m in models:
   admin.site.register(m)
