from django.db import models
from django.contrib.auth.models import User


from core.models import NameBaseConfig, BasicConfiguration

# TODO: add user on save: https://stackoverflow.com/questions/2991365/how-to-auto-insert-the-current-user-when-creating-an-object-in-django-admin

class Ceremony(NameBaseConfig):
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"Name: {self.name}"


class Event(NameBaseConfig):
    from hosts.models import Volunteer
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)
    event_broadcast_url = models.URLField(verbose_name="event_broadcast_url", blank=True, null=True)
    managed_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    max_participation_limit = models.IntegerField(default=100)

    def __str__(self):
        return f"Name: {self.name} Managed by: {self.managed_by.user.username}"
