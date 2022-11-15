from django.shortcuts import render
from flight_management.models import Flight
from login import views

def flightmonitoringview(request):
    all_flights = Flight.objects.all()
    context = {
        'all_flights' : all_flights,
        'selectedRole' : str(views.role)
    }
    return render(request, "home.html", context)
