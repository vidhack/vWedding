from rest_framework import serializers
from guests.models import GuestGroupmember


class GuestGroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestGroupmember
        fields = ['id', 'guest', 'sub_event.namue', 'invitation_sent', 'attended']


