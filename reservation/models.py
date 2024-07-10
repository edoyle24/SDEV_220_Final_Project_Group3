from django.conf import settings
from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateTimeField(blank=True, null=True)

    def reserve(self):
        self.scheduled_date = timezone.now()
        self.save()

    def __str__(self):
        return self.User