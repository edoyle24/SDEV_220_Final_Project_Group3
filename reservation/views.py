from django.shortcuts import render

def index(request):
    return render(request, 'reservation/index.html', {})
def appointment(request):
    return render(request, 'reservation/appointment.html', {})
def reservations(request):
    return render(request, 'reservation/reservations.html', {})
def staff(request):
    return render(request, 'reservation/staff.html', {})
