from django.contrib import admin
from apps.traffic.models import Camera, Event

admin.site.register(Camera)
admin.site.register(Event)