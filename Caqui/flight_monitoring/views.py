from django.shortcuts import render

# Create your views here.
def flightmonitoringview(request):
    return render(request, "home.html")