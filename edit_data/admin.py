from django.contrib import admin
from edit_data.models import Man, Event

# Register your models here.

class EventAdnin(admin.ModelAdmin):
    list_display = ('member0', 'type', 'date')



admin.site.register(Man)
admin.site.register(Event, EventAdnin)
