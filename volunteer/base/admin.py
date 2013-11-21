from django.contrib import admin
from .models import Event, EventSlot, Volunteer
from django_mailman.models import List

admin.site.register(Event)
admin.site.register(EventSlot)
admin.site.register(Volunteer)
admin.site.register(List)