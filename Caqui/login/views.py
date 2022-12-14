from django.shortcuts import render
from .forms import FormLoginUser
from flight_management.models import User
from flight_monitoring import views as flightmonitoringviews
from flight_management.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
role = None

def loginview(request):

    if request.method == 'POST':
        form = FormLoginUser(request.POST)
        try:
            user = User.objects.get(tx_username=request.POST['login'])
        except User.DoesNotExist:
            user = None
            if "load_count" in request.session:
                count = request.session["load_count"] + 1
            else:
                count = 1

            request.session["load_count"] = count
            if(request.session["load_count"] >= 3):
                request.session["load_count"] = 0
                return render(request, 'error.html')
        else:
            if user.tx_hash_key == request.POST['password']:
                context = {'selectedRole':user.tx_username}
                request.session["load_count"] = 0
                global role
                role = user.tx_username
                return HttpResponseRedirect(reverse(flightmonitoringviews.flightmonitoringview))
            else:
                if "load_count" in request.session:
                    count = request.session["load_count"] + 1
                else:
                    count = 1

                request.session["load_count"] = count
                if(request.session["load_count"] >= 3):
                    request.session["load_count"] = 0
                    return render(request, 'error.html')
    else:
        role = None
        form = FormLoginUser()
    
    context = {'form': form}

    return render(request, 'login.html', context)