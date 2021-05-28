from django.contrib import admin

from guests.models import Guest, GuestGroup, GuestGroupmember

class GuestAdmin(admin.ModelAdmin):
    pass


class GuestGroupAdmin(admin.ModelAdmin):
    pass


class GuestGroupMembersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Guest, GuestAdmin)
admin.site.register(GuestGroup, GuestGroupAdmin)
admin.site.register(GuestGroupmember, GuestGroupMembersAdmin)
