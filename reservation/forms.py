from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['fullname', 'dob', 'phone','email','dentist', 'date', 'time']