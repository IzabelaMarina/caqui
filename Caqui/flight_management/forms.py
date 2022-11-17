from django import forms
from flight_management.enums import Status, AirportCodes

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormUpdateStatus(forms.Form):

    code_flight = forms.CharField(label='Código', max_length=8, required=False)
    date_departure = forms.DateTimeField(label='Data de partida', widget=DateInput, required=False)
    date_arrival = forms.DateTimeField(label='Data de chegada', widget=DateInput, required=False)
    select_status = forms.ChoiceField(label='Status', choices=Status.choices, required=False)

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import datetime  # for checking renewal date range.
import pytz
utc=pytz.UTC

class CreateFlightForm(forms.Form):
    tx_code = forms.CharField(
            label='Código',
            # length=7,
            validators=[
                RegexValidator(
                    '^[A-Z]{3}\d{4}$',
                    message="Código de voo deve ter 3 letras maiúsculas seguidas por 4 dígitos."
                )
            ],
            required=True)
    dt_est_departure = forms.DateTimeField(
            label='Data de Partida Estimada', 
            widget=DateInput)

    dt_est_arrival = forms.DateTimeField(
            label='Data de Chegada Estimada', 
            widget=DateInput)
    nm_origin = forms.ChoiceField(label='Origem',choices=AirportCodes.choices, required=True)
    nm_destination = forms.ChoiceField(label='Destino',choices=AirportCodes.choices, required=True)

    def clean_dt_est_departure(self):
        data = self.cleaned_data['dt_est_departure']
        data = data.replace(tzinfo=utc)

        # Check date is not in past.
        if data < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Data inválida - voo no passado! Não estamos em \'De volta para o futuro\'!'))

        # Remember to always return the cleaned data.
        return data

    def clean_dt_est_arrival(self):
        data = self.cleaned_data['dt_est_arrival']
        data = data.replace(tzinfo=utc)

        # Check date is not in past.
        if data < utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Data inválida - voo no passado! Não estamos em \'De volta para o futuro\'!'))
        
        # Remember to always return the cleaned data.
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        dt_est_departure = cleaned_data.get("dt_est_departure")
        dt_est_arrival = cleaned_data.get("dt_est_arrival")

        if dt_est_departure and dt_est_arrival:
            if dt_est_arrival < dt_est_departure:
                raise ValidationError(_('Avião não pode chegar antes de partir'))

        nm_origin = cleaned_data.get("nm_origin")
        nm_destination = cleaned_data.get("nm_destination")

        if nm_origin and nm_destination:
            if (AirportCodes.GRU not in nm_origin) and (AirportCodes.GRU not in nm_destination):
                raise ValidationError(_('Proibido criar voo que não envolva noos aeroporto: GRU'))
            elif (nm_origin == AirportCodes.GRU) and (nm_destination == AirportCodes.GRU):
                raise ValidationError(_('Proibido criar voo que parta e chegue do mesmo aeroporto.'))
            
        return cleaned_data
