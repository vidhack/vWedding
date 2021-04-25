from django.db import models
from django.contrib.auth.models import User


from core.models import NameBaseConfig, BasicConfiguration
from hosts.models import Client, Volunteer

# TODO: add user on save: https://stackoverflow.com/questions/2991365/how-to-auto-insert-the-current-user-when-creating-an-object-in-django-admin

class Event(NameBaseConfig):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    volunteers = models.ManyToManyField(Volunteer, related_name="event")


class SubEvent(NameBaseConfig):
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_broadcast_url = models.URLField(verbose_name="event_broadcast_url", blank=True, null=True)
    managed_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    max_participation_limit = models.IntegerField(default=100)
