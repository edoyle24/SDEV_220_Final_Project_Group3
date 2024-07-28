from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Dentist, Appointment
from .forms import AppointmentForm
from django.contrib.auth import logout

def index(request):
    return redirect('home')

def home(request):
    return render(request, 'reservation/home.html', {})

def appointment(request):
    return render(request, 'reservation/appointment.html', {})

@login_required
def reservations(request):
    posts = Appointment.objects.all()
    return render(request, 'reservation/reservations.html', {'posts': posts})
def staff(request):
    staff = Dentist.objects.all()
    return render(request, 'reservation/staff.html', {'staff': staff})

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
    return render(request, 'reservation/create_appointment.html', {'form': form})

@login_required
def appointment_success(request):
    return render(request, 'reservation/appointment_success.html', {})

@login_required
def user_detail(request, pk):
    post = get_object_or_404(Appointment, pk=pk)
    return render(request, 'reservation/user_detail.html', {'post': post})

@login_required
def appointment_remove(request, pk):
    post = get_object_or_404(Appointment, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('reservations')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})