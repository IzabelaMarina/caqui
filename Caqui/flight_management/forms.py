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
from django.core.validators import RegexValidator
import datetime  # for checking renewal date range.
import pytz
utc=pytz.UTC

class CreateFlightForm(forms.Form):
    tx_code = forms.CharField(
            label='Flight Code',
            # length=7,
            validators=[
                RegexValidator(
                    '^[A-Z]{3}\d{4}$',
                    message="Flight Code must consist of 3 uppercase letters followed by 4 digits."
                )
            ],
            required=True)
    dt_est_departure = forms.DateTimeField(
            label='Estimated Departure Datetime', 
            widget=DateInput)

    dt_est_arrival = forms.DateTimeField(
            label='Estimated Arrival Datetime', 
            widget=DateInput)
    nm_origin = forms.ChoiceField(label='Origin',choices=AirportCodes.choices, required=True)
    nm_destination = forms.ChoiceField(label='Destination',choices=AirportCodes.choices, required=True)

    def clean_dt_est_departure(self):
        data = self.cleaned_data['dt_est_departure']
        data = data.replace(tzinfo=utc)

        # Check date is not in past.
        if data < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Invalid date - flight in the past\nThis isn\'t back to the future!'))

        # Remember to always return the cleaned data.
        return data

    def clean_dt_est_arrival(self):
        data = self.cleaned_data['dt_est_arrival']
        data = data.replace(tzinfo=utc)

        # Check date is not in past.
        if data < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Invalid date - flight in the past\nThis isn\'t back to the future!'))
        
        # Remember to always return the cleaned data.
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        dt_est_departure = cleaned_data.get("dt_est_departure")
        dt_est_arrival = cleaned_data.get("dt_est_arrival")

        if dt_est_departure and dt_est_arrival:
            if dt_est_arrival < dt_est_departure:
                raise ValidationError(_('Plane cannot arrive before it departs.'))

        nm_origin = cleaned_data.get("nm_origin")
        nm_destination = cleaned_data.get("nm_destination")

        if nm_origin and nm_destination:
            if (AirportCodes.GRU not in nm_origin) and (AirportCodes.GRU not in nm_destination):
                raise ValidationError(_('Cannot create a flight that does not involve our airport: GRU'))
            elif (nm_origin == AirportCodes.GRU) and (nm_destination == AirportCodes.GRU):
                raise ValidationError(_('Cannot create a flight that departs and arrives at the same airport'))
            
        return cleaned_data
