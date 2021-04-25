from django.contrib import admin

from hosts.models import Client, Volunteer


class ClientAdmin(admin.ModelAdmin):
    pass


class VolunteerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
