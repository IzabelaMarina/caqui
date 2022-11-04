from django.shortcuts import render
from datetime import datetime
from flight_management.enums import Role
from flight_management.models import FlightStatus, Flight, User
#from django.core import serializers

# Create your views here.
def flightmonitoringview(request,selectedRole):
    all_flights = Flight.objects.all()
    context = {
        'all_flights' : all_flights,
    }
    return render(request, "home.html", context)

def flightmonitoringview_temporary(request):
    all_flights = Flight.objects.all()
    context = {
        'all_flights' : all_flights,
    }
    return render(request, "home.html", context)