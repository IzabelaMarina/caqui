from django.shortcuts import render

# Create your views here.
def flightmanagementview(request):
    return render(request, "crud.html")

def flightupdateview(request):
    return render(request, "update.html")