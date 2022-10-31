from django import forms
from flight_management.enums import Status 

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormUpdateStatus(forms.Form):
    code_flight = forms.CharField(label='Código de Voo', max_length=8, required=False)
    date_departure = forms.DateTimeField(label='Data de Partida', widget=DateInput, required=False)
    date_arrival = forms.DateTimeField(label='Data de Chegada', widget=DateInput, required=False)
    select_status = forms.ChoiceField(label='Status de Voo', choices=Status.choices, required=False)
