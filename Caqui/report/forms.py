from django import forms
from django.forms import DateInput
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import pytz
utc=pytz.UTC

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormDates(forms.Form):
    min_date = forms.DateTimeField(label='Data de início', widget=forms.DateInput(attrs={'type': "date", 'class': "form-control", 'placeholder':"dd/mm/yyyy"}), required=True)
    max_date = forms.DateTimeField(label='Data de fim', widget=forms.DateInput(attrs={'type': "date", 'class': "form-control", 'placeholder':"dd/mm/yyyy"}), required=True)

    def clean_min_date(self):
        data = self.cleaned_data['min_date']
        data = data.replace(tzinfo=utc)

        # Check date is not in future.
        if data > utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Data inválida. Relatórios não podem ser gerados para datas futuras.'))

        # Remember to always return the cleaned data.
        return data

    def clean_max_date(self):
        data = self.cleaned_data['max_date']
        data = data.replace(tzinfo=utc)

        # Check date is not in future.
        if data > utc.localize(datetime.datetime.now()):
            raise ValidationError(_('Data inválida. Relatórios não podem ser gerados para datas futuras.'))
        
        # Remember to always return the cleaned data.
        return data

    def clean(self):
        cleaned_data = super().clean()
        min_date = cleaned_data.get("min_date")
        max_date = cleaned_data.get("max_date")

        if min_date and max_date:
            if max_date < min_date:
                raise ValidationError(_('Data final não pode ser menor do que a data inicial!'))            
        return cleaned_data