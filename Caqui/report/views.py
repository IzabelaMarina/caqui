from django.shortcuts import render

# Create your views here.
def reportview(request):
    return render(request, "report.html")