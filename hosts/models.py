from django.db import models
from django.contrib.auth.models import User


from core.models import NameBaseConfig, BasicConfiguration
# Create your models here.

class Client(NameBaseConfig):
    from events.models import Ceremony
    ceremony = models.OneToOneField(Ceremony, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_till = models.DateTimeField()


class Volunteer(BasicConfiguration):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="as_volunteer")
    added_by = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="added_by_clients")

    def __str__(self):
        return f"name: {self.user.username} added_by: {self.added_by.user.username}"
