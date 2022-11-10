from django import forms
from flight_management.enums import Status, AirportCodes

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormUpdateStatus(forms.Form):

    code_flight = forms.CharField(label='Código de Voo', max_length=8, required=False)
    date_departure = forms.DateTimeField(label='Data de Partida', widget=DateInput, required=False)
    date_arrival = forms.DateTimeField(label='Data de Chegada', widget=DateInput, required=False)
    select_status = forms.ChoiceField(label='Status de Voo', choices=Status.choices, required=False)

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime  # for checking renewal date range.
import pytz
utc=pytz.UTC

class CreateFlightForm(forms.Form):
    tx_code = forms.CharField(label='Flight Code', max_length=8, required=True)
    dt_est_departure = forms.DateTimeField(
            label='Datetime of departure', 
            widget=DateInput, 
            help_text="Enter the estimated departure datetime of the flight.")

    dt_est_arrival = forms.DateTimeField(
            label='Datetime of arrival', 
            widget=DateInput, 
            help_text="Enter the estimated arrival datetime of the flight.")
    nm_origin = forms.ChoiceField(choices=AirportCodes.choices, required=True)
    nm_destination = forms.ChoiceField(choices=AirportCodes.choices, required=True)

    def clean_dt_est_departure(self):
        data0 = self.cleaned_data['dt_est_departure']
        data0 = data0.replace(tzinfo=utc)

        # Check date is not in past.
        if data0 < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Invalid date - flight in the past\nThis isn\'t back to the future!'))

        # Remember to always return the cleaned data.
        return data0

    def clean_dt_est_arrival(self):
        data1 = self.cleaned_data['dt_est_arrival']
        data1 = data1.replace(tzinfo=utc)

        # Check date is not in past.
        if data1 < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Invalid date - flight in the past\nThis isn\'t back to the future!'))
        
        # Remember to always return the cleaned data.
        return data1
    
    # regex
    def clean_tx_code(self):
        data = 0
        return data

    # nosso aeroporto
    def clean_nm_origin(self):
        data = 0
        return data

    def clean_nm_destination(self):
        data = 0
        return data