from django.http import HttpResponse
from django.shortcuts import redirect, render
from flight_management.models import Flight
from . import forms 
from django.views.generic import TemplateView
from datetime import datetime
from django.core.cache import cache

from .utils import render_to_pdf

# Create your views here.
class ReportView(TemplateView):

    def get(self,request):
        formDates = forms.FormDates()
        formCode = forms.FormCode()
        return render(request, "report.html", {'formDates': formDates, 'formCode': formCode})

    def post(self,request):
        if 'date_report' in request.POST:
            formDates = forms.FormDates(request.POST)
            if formDates.is_valid():
                request.session['minDate'] = str(formDates.cleaned_data['min_date'])
                request.session['maxDate'] = str(formDates.cleaned_data['max_date'])
        elif 'code_report' in request.POST:
            formCode = forms.FormCode(request.POST)
            if formCode.is_valid():
                request.session['flight_code'] = formCode.cleaned_data['flight_code']
        formDates = forms.FormDates()
        formCode = forms.FormCode()
        return redirect('/report/flightreport')

def reportflightview(request):
    if ((request.session.get('minDate') != 'None' and request.session.get('minDate') is not None) and (request.session.get('maxDate') != 'None' and request.session.get('maxDate') is not None)):
        print("date")
        minDate = datetime.strptime(request.session.get('minDate'),'%Y-%m-%d %H:%M:%S%z')
        maxDate = datetime.strptime(request.session.get('maxDate'),'%Y-%m-%d %H:%M:%S%z')
        dataset = Flight.objects.filter(dt_est_departure__lte = maxDate, dt_est_departure__gte = minDate).values('id','tx_code','dt_est_departure','dt_est_arrival','nm_origin','nm_destination','fk_flightstatus__nm_status','fk_flightstatus__dt_departure','fk_flightstatus__dt_arrival')
    elif (request.session.get('flight_code') != 'None' and request.session.get('flight_code') is not None):
        print("code")
        flightCode = request.session.get('flight_code')
        dataset = Flight.objects.filter(tx_code = flightCode).values('id','tx_code','dt_est_departure','dt_est_arrival','nm_origin','nm_destination','fk_flightstatus__nm_status','fk_flightstatus__dt_departure','fk_flightstatus__dt_arrival')
    else:
        print("else")
        dataset = []
    request.session.clear()
    cache.set('dataset', dataset)

    return render(request, "flightreport.html", {'dataset': dataset})

def export_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = Report' + \
        str(datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    result = render_to_pdf('pdf-output.html', {'dataset': cache.get('dataset')})
    response.write(result)

    return response