from django.shortcuts import render
from flight_management.models import FlightStatus, Flight, User
#from django.core import serializers

# Create your views here.
def flightmanagementview(request):
    return render(request, "crud.html")

def flightupdateview(request):
    all_flights = Flight.objects.all()
    context = {'all_flights' : all_flights}
    return render(request, "update.html", context)