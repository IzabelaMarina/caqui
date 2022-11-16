from django.http import HttpResponse
from django.shortcuts import redirect, render
from flight_management.models import Flight
from . import forms 
from django.views.generic import TemplateView
from datetime import datetime
from django.core.cache import cache
import operator

from .utils import render_to_pdf

# Create your views here.
class ReportView(TemplateView):

    def get(self,request):
        request.session.clear()
        formDates = forms.FormDates()
        formCode = forms.FormCode()
        return render(request, "report.html", {'formDates': formDates, 'formCode': formCode})

    def post(self,request):

        formDates = forms.FormDates(request.POST)
        if formDates.is_valid():
            request.session['minDate'] = str(formDates.cleaned_data['min_date'])
            request.session['maxDate'] = str(formDates.cleaned_data['max_date'])
        if 'cmpny_report' in request.POST:
            request.session['cmpny_report'] = True
        else:
            request.session['cmpny_report'] = False
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
    cmpnyData = False
    if ((request.session.get('minDate') != 'None' and request.session.get('minDate') is not None) and (request.session.get('maxDate') != 'None' and request.session.get('maxDate') is not None)):
        minDate = datetime.strptime(request.session.get('minDate'),'%Y-%m-%d %H:%M:%S%z')
        maxDate = datetime.strptime(request.session.get('maxDate'),'%Y-%m-%d %H:%M:%S%z')
        dataset = Flight.objects.filter(dt_est_departure__lte = maxDate, dt_est_departure__gte = minDate).values('id','tx_code','dt_est_departure','dt_est_arrival','nm_origin','nm_destination','fk_flightstatus__nm_status','fk_flightstatus__dt_departure','fk_flightstatus__dt_arrival')
        if request.session.get('cmpny_report'):
            cmpnyData = True
            companies={}
            for flight in dataset:
                flight['company'] = flight['tx_code'][0:3]
                if companies.get(flight['company']) == None:
                    companies.update({flight['company']:1})
                else:
                    companies[flight['company']] += 1
            sorted_cmpns = sorted(companies.items(),key=operator.itemgetter(1))
            cache.set('companies',sorted_cmpns)
            dataset = dataset.order_by('tx_code')
    else:
        dataset = []
    cache.set('dataset', dataset)
    if cmpnyData:
        return render(request, "companyreport.html", {'dataset': dataset, 'companies': sorted_cmpns})
    else:
        return render(request, "flightreport.html", {'dataset': dataset})

def export_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = FlightReport-' + \
        str(datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    result = render_to_pdf('pdf-output.html', {'dataset': cache.get('dataset')})
    response.write(result)

    return response

def export_pdf_cmpny(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = CompanyReport-' + \
        str(datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    result = render_to_pdf('pdf-output-cmpny.html', {'dataset': cache.get('dataset'), 'companies': cache.get('companies')})
    response.write(result)

    return response