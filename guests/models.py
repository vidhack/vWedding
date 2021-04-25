from django.db import models
from django.contrib.auth.models import User


from core.models import NameBaseConfig, BasicConfiguration
from events.models import Event, SubEvent
from hosts.models import Volunteer


class Guest(BasicConfiguration):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    added_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.user.username} event: {self.event.name} added_by: {self.added_by.user.username}"

class GuestGroup(NameBaseConfig):
    created_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    members = models.ManyToManyField(Guest, related_name="groups")

    def __str__(self):
        return f"{self.name}  {self.slug}"



class GuestInvitedEvent(BasicConfiguration):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    sub_event = models.ForeignKey(SubEvent, on_delete=models.CASCADE)
    invitation_sent = models.BooleanField(default=False)
    attended = models.BooleanField()

    def __str__(self):
        return f"name: {self.guest.user.username} sub-event: {self.sub_event.name}"

