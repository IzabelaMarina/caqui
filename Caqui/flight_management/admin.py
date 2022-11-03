from django.contrib import admin
from flight_management.models import FlightStatus, Flight, User

admin.site.register(User)
admin.site.register(FlightStatus)
admin.site.register(Flight)