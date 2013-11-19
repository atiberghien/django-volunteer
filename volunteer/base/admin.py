from django.contrib import admin
from .models import Event, EventSlot, Volunteer

admin.site.register(Event)
admin.site.register(EventSlot)
admin.site.register(Volunteer)