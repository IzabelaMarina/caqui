from django.shortcuts import render
from datetime import datetime
from flight_management.models import FlightStatus, Flight, User

# Create your views here.
def flightmonitoringview(request):
    return render(request, "home.html")

def update_status(request):

    allFlights = Flight.objects.all()
    print(allFlights)
    return render(request,"update.html",{"flights": allFlights})
