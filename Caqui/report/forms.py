from django import forms
from django import forms
from django.forms import DateInput

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormDates(forms.Form):
    min_date = forms.DateTimeField(label='Data de início', widget=forms.DateInput(attrs={'type': "date", 'class': "form-control", 'placeholder':"dd/mm/yyyy"}), required=False)
    max_date = forms.DateTimeField(label='Data de fim', widget=forms.DateInput(attrs={'type': "date", 'class': "form-control", 'placeholder':"dd/mm/yyyy"}), required=False)

class FormCode(forms.Form):
    flight_code = forms.CharField(label='Código de Voo', max_length=8, widget = forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder':"Insira um código de voo"}), required=False)