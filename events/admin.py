from django.contrib import admin

from events.models import Event, SubEvent

class EventAdmin(admin.ModelAdmin):
    pass


class SubEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(SubEvent, SubEventAdmin)
