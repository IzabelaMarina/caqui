from django.shortcuts import render
from flight_management import views as flightmanagementviews
from flight_management.models import User, Flight, FlightStatus
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .forms import FormUpdateStatus
from flight_management.enums import Status, Role
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse

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

class FlightCreate(CreateView):
    model = Flight
    fields = ['tx_code','dt_est_departure','dt_est_arrival', 'nm_origin', 'nm_destination']

class FlightUpdate(UpdateView):
    model = Flight
    fields = ['fk_flightstatus','dt_est_departure','dt_est_arrival']

class FlightDelete(DeleteView):
    model = Flight
    success_url = reverse_lazy('flight')

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
            if ((listStatus.index(request.POST['select_status']) - listStatus.index(flightstatus.nm_status) == 1)):
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
                print("aaa")
                return render(request, 'edit2.html', context)
    else:
        form = FormUpdateStatus()
    
    context = {'form': form}

    return render(request, 'edit.html', context)