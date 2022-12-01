import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse

from flight_management import views as flightmanagementviews
from flight_management.models import User, Flight, FlightStatus
from flight_management.enums import AirportCodes, Status
from flight_management.forms import CreateFlightForm, FormUpdateStatus, UpdateFlightForm

listStatus = ["Previsto", "Cancelado", "Embarcando", "Programado", "Taxiando", "Pronto", "Autorizado", "Em Voo", "Aterrissado", "Desembarcando"]

# Create your views here.
def index(request):
    return render(request, "crud.html")

class UserListView(generic.ListView):
    model = User
    paginate_by = 10

class UserDetailView(generic.DetailView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ['tx_name','nm_role','tx_username','tx_hash_key']

class UserUpdate(UpdateView):
    model = User
    fields = ['tx_name','nm_role','tx_hash_key']

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user')

class FlightListView(generic.ListView):
    model = Flight
    paginate_by = 10

class FlightDetailView(generic.DetailView):
    model = Flight

# class FlightCreate(CreateView):
#     model = Flight
#     fields = ['tx_code','dt_est_departure','dt_est_arrival', 'nm_origin', 'nm_destination']

def create_flight(request):
    flight_status = FlightStatus()
    flight_status.save()
    
    flight = Flight(fk_flightstatus=flight_status)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CreateFlightForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            flight.tx_code = form.cleaned_data['tx_code']
            flight.nm_destination = form.cleaned_data['nm_destination']
            flight.nm_origin = form.cleaned_data['nm_origin']
            flight.dt_est_departure = form.cleaned_data['dt_est_departure']
            flight.dt_est_arrival = form.cleaned_data['dt_est_arrival']

            flight_status.dt_departure = flight.dt_est_departure
            flight_status.dt_arrival = flight.dt_est_arrival
            if flight.nm_destination == AirportCodes.GRU:
                flight_status.nm_status = FlightStatus(nm_status=Status.EM_VOO).nm_status
            flight_status.save()
            flight.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('flight'))

    # If this is a GET (or any other method) create the default form
    else:
        proposed_arrival_date = datetime.datetime.now()
        proposed_departure_date = datetime.datetime.now()
        form = CreateFlightForm(initial={'tx_code': "FOO9999",'dt_est_departure': proposed_departure_date,'dt_est_arrival': proposed_arrival_date, 'nm_origin': AirportCodes.GRU, 'nm_destination': AirportCodes.GRU})

    context = {
        'form': form,
        'flight': flight,
    }

    return render(request, 'flight_management/flight_create.html', context)

# class FlightUpdate(UpdateView):
#     model = Flight
#     # fields = ['fk_flightstatus.id','dt_est_departure','dt_est_arrival']
#     fields = ['dt_est_departure','dt_est_arrival']
#     success_url = reverse_lazy('flight')
#     # template_name = 'flight_update.html'

def update_flight(request, pk):
    flight = get_object_or_404(Flight, id = pk)

    if request.method == 'POST':
        form = UpdateFlightForm(request.POST)

        if form.is_valid():
            flight.dt_est_departure = form.cleaned_data['dt_est_departure']
            flight.dt_est_arrival = form.cleaned_data['dt_est_arrival']
            flight.save()
            return HttpResponseRedirect(reverse('flight'))

    # If this is a GET (or any other method) create the default form
    else:
        proposed_arrival_date = flight.dt_est_arrival
        proposed_departure_date = flight.dt_est_departure
        form = UpdateFlightForm(initial={'dt_est_departure': proposed_departure_date,'dt_est_arrival': proposed_arrival_date})

    context = {
        'form': form,
        'flight': flight,
    }

    return render(request, 'flight_management/flight_update.html', context)

class FlightDelete(DeleteView):
    model = Flight
    success_url = reverse_lazy('flight')

def flightupdateview(request):
    all_flights = Flight.objects.all()
    all_status_flights = FlightStatus.objects.all()
    context = {'all_flights' : all_flights, 'all_status_flights' : all_status_flights}
    return render(request, "update.html", context)


def update_status(request, pk):
    flightstatus = get_object_or_404(FlightStatus, id = pk)

    if request.method == 'POST':
        form = FormUpdateStatus(request.POST)

        dif_index = listStatus.index(request.POST['select_status']) - listStatus.index(flightstatus.nm_status)
        if (dif_index == 1 or dif_index == 0):
            if request.POST['select_status'] != "":
                flightstatus.nm_status = request.POST['select_status']
            if request.POST['date_departure'] != "":
                flightstatus.dt_departure = request.POST['date_departure']
            if request.POST['date_arrival'] != "":
                flightstatus.dt_arrival = request.POST['date_arrival']
            flightstatus.save()
            return redirect(reverse(flightmanagementviews.flightupdateview))

        elif (listStatus.index(flightstatus.nm_status) == 0 and listStatus.index(request.POST['select_status']) == 2):
            if request.POST['select_status'] != "":
                flightstatus.nm_status = request.POST['select_status']
            if request.POST['date_departure'] != "":
                flightstatus.dt_departure = request.POST['date_departure']
            if request.POST['date_arrival'] != "":
                flightstatus.dt_arrival = request.POST['date_arrival']
            flightstatus.save()
            return redirect(reverse(flightmanagementviews.flightupdateview))
        
        else:
            form = FormUpdateStatus()
            context = {'form': form}
            return render(request, 'edit_not_possible.html', context)
    else:
        form = FormUpdateStatus()
    
    context = {
        'form': form,
        'flightstatus': flightstatus,
    }

    return render(request, 'edit.html', context)
