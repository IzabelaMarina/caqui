from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from flight_management.models import Flight
from . import forms 
from django.views.generic import TemplateView

# Create your views here.
class ReportView(TemplateView):

    def get(self,request):
        formDates = forms.FormDates()
        formCode = forms.FormCode()
        return render(request, "report.html", {'formDates': formDates, 'formCode': formCode})

    def post(self,request):
        formDates = forms.FormDates(request.POST)
        formCode = forms.FormCode(request.POST)
        if formDates.is_valid():
            request.session['minDate'] = formDates.cleaned_data['min_date']
            request.session['maxDate'] = formDates.cleaned_data['max_date']
        elif formCode.is_valid():
            request.session['flight_code'] = formCode.cleaned_data['flight_code']
        return render(request, "report.html", {'formDates': formDates, 'formCode': formCode})

def reportflightview(request):
    return render(request, "flightreport.html")

def flight_data(request):
    dataset = Flight.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)