from django.conf import settings
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=180, default="new Event")
    description = models.CharField(max_length=300, null=True)
    place = models.CharField(max_length=180, null=True)
    address = models.CharField(max_length=180, null=True)
    created_At = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=False, null=True)
    mode = models.BooleanField(null=True, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, default=1)

    def __str__(self):
        return "Event Data is Here"
