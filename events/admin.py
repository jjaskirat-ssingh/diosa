from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display', 'venue', 'event_date')
    list_display_links = ('id', 'title')
    list_filter = ('venue',)
    list_editable = ('display',)
    search_fields = ('title', 'description', 'venue', 'event_date')
    list_per_page = 25

admin.site.register(Event, EventAdmin)

