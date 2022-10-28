from django import forms
from flight_management.enums import Status 

class FormUpdateStatus(forms.Form):
    code_flight = forms.CharField(label='Código de Voo', max_length=8)
    #date_departure = forms.DateTimeField(label='Data de Partida')
    #date_arrival = forms.DateTimeField(label='Data de Chegada')
    select_status = forms.ChoiceField(label='Status de Voo', choices=Status.choices)
