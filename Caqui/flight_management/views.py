from asyncio.windows_events import NULL
from django.shortcuts import render
from flight_management.models import FlightStatus, Flight, User
from .forms import FormUpdateStatus
from flight_management.enums import Status 
#from django.core import serializers

# Create your views here.
def flightmanagementview(request):
    return render(request, "crud.html")

def flightupdateview(request):
    all_flights = Flight.objects.all()
    all_status_flights = FlightStatus.objects.all()
    context = {'all_flights' : all_flights, 'all_status_flights' : all_status_flights}
    return render(request, "update.html", context)

def update_status(request):
    if request.method == 'POST':
        form = FormUpdateStatus(request.POST)
        try:
            flight = Flight.objects.get(tx_code=request.POST['code_flight'])
        except Flight.DoesNotExist:
            flight = None
        else:
            flightstatus = flight.fk_flightstatus
            if request.POST['select_status'] != "":
                flightstatus.nm_status = request.POST['select_status']
            if request.POST['date_departure'] != "":
                flightstatus.dt_departure = request.POST['date_departure']
            if request.POST['date_arrival'] != "":
                flightstatus.dt_arrival = request.POST['date_arrival']
            flightstatus.save()
    else:
        form = FormUpdateStatus()
    
    context = {'form': form}

    return render(request, 'edit.html', context)
