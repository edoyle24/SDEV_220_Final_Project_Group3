from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/appointment', views.appointment, name='appointment'),
    path('index/', views.home, name='home'),
    path('index/staff', views.staff, name='staff'),
    path('index/reservations', views.reservations, name='reservations'),
    path('index/create', views.create_appointment, name='create_appointment'),
    path('index/success', views.appointment_success, name='appointment_success'),
    path('index/appointment/<int:pk>/', views.user_detail, name='user_detail'),
    path('index/appointment/<pk>/remove/', views.appointment_remove, name='appointment_remove'),
    path('index/logged_out', views.user_logout, name="user_logout"),
]