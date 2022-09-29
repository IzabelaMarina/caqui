from django.shortcuts import render

# Create your views here.
def flightmanagementview(request):
    return render(request, "home_flight.html")