from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/appointment', views.appointment, name='appointment'),
    path('index/staff', views.staff, name='staff'),
    path('index/reservations', views.reservations, name='reservations'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
]