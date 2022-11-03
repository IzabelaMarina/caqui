from django.shortcuts import render
from .forms import FormLoginUser
from flight_management.models import User
from flight_monitoring import views as flightmonitoringviews
from flight_management.models import FlightStatus, Flight, User
from django.shortcuts import redirect
from django.urls import reverse

from flight_management.enums import Role, Status

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        form = FormLoginUser(request.POST)
        try:
            user = User.objects.get(tx_username=request.POST['login'])
            print(user)
        except User.DoesNotExist:
            user = None
        else:
            if user.tx_hash_key == request.POST['password']:
                print("SUCESSO")
                paramater = {
                    'selectedRole': user.tx_username
                }
                return redirect(reverse(flightmonitoringviews.flightmonitoringview,kwargs={}))
    else:
        form = FormLoginUser()
    
    context = {'form': form}

    return render(request, 'login.html', context)