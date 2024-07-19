from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dentist, Appointment
from .forms import AppointmentForm

def index(request):
    return render(request, 'reservation/index.html', {})
def appointment(request):
    return render(request, 'reservation/appointment.html', {})
def reservations(request):
    return render(request, 'reservation/reservations.html', {})
def staff(request):
    return render(request, 'reservation/staff.html', {})

@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'reservations/create_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'reservations/appointment_success.html', {})

