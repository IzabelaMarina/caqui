from django.shortcuts import render

from flight_management.enums import Role, Status

# Create your views here.
def loginview(request):
    return render(request, "login.html")