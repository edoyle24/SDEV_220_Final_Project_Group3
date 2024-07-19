from django.contrib import admin
from .models import Dentist, Appointment

admin.site.register(Dentist)
admin.site.register(Appointment)