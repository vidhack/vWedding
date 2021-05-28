from django.contrib import admin

from events.models import Ceremony, Event

class CeremonyAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ceremony, CeremonyAdmin)
admin.site.register(Event, EventAdmin)
