from rest_framework import viewsets


from guests.models import GuestGroupmember
from guests.serializers import GuestGroupMembersSerializer

class GuestGroupMembersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GuestGroupMembersSerializer

    def get_queryset(self):
        queryset = GuestGroupmember.objects.filter(guest__user = self.request.user)
