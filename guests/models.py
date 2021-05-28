from django.db import models
from django.contrib.auth.models import User


from core.models import NameBaseConfig, BasicConfiguration
from events.models import Ceremony, Event
from hosts.models import Volunteer


class Guest(BasicConfiguration):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)
    added_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.user.username} event: {self.ceremony.name} added_by: {self.added_by.user.username}"

class GuestGroup(NameBaseConfig):
    created_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    members = models.ManyToManyField(Guest, related_name="groups", through="GuestGroupmember")

    def __str__(self):
        return f"{self.name}  {self.slug}"


class GuestGroupmember(BasicConfiguration):
    # Assigning the Group with Event populate GuestEventInvitedMember
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    group = models.ForeignKey(GuestGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.guest.user.username} sub-event: {self.group.name}"


class GroupEventInvitedMember(BasicConfiguration):
    # On save on delete modify GuestEventInvitedMember
    group = models.ForeignKey(GuestGroup, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class GuestEventInvitedMember(BasicConfiguration):
    #TODO: Might need to delete it
    guest = models.ForeignKey(GuestGroupmember, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invitation_sent = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"name: {self.guest.user.username} sub-event: {self.event.name}"
