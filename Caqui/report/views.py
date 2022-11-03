from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from flight_management.models import Flight
from . import forms 
from django.views.generic import TemplateView
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
import json

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
            request.session['minDate'] = str(formDates.cleaned_data['min_date'])
            request.session['maxDate'] = str(formDates.cleaned_data['max_date'])
        elif formCode.is_valid():
            request.session['flight_code'] = formCode.cleaned_data['flight_code']
        return render(request, "report.html", {'formDates': formDates, 'formCode': formCode})

def reportflightview(request):
    return render(request, "flightreport.html")

def flight_data(request):
    if (request.session.get('minDate') != 'None' and request.session.get('maxDate') != 'None'):
        minDate = datetime.strptime(request.session.get('minDate'),'%Y-%m-%d %H:%M:%S%z')
        maxDate = datetime.strptime(request.session.get('maxDate'),'%Y-%m-%d %H:%M:%S%z')
        dataset = Flight.objects.filter(dt_est_departure__lte = maxDate, dt_est_departure__gte = minDate).values()
    elif (request.session.get('flight_code') != 'None'):
        flightCode = request.session.get('flight_code')
        dataset = Flight.objects.filter(tx_code=flightCode).values()
    else:
        dataset = []
    dataset_list = list(dataset)
    data = json.dumps(dataset_list, cls = DjangoJSONEncoder)
    return JsonResponse(data, safe=False)