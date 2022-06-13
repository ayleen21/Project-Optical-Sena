from django.contrib import admin
from app.login.models import *
from app.patients.models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(medicalRecords)
admin.site.register(Hobbies)

