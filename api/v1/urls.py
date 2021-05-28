from django.urls import path, include
from rest_framework import routers

from guests.views import GuestGroupMembersViewSet


router = routers.DefaultRouter()
router.register(r'guestgroupmembers', GuestGroupMembersViewSet, basename="GuestGroupMembers")

urlpatterns = router.urls
