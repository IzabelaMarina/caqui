from django import forms

class FormLoginUser(forms.Form):

    login = forms.CharField(max_length=42,label='Login')
    password = password = forms.CharField(max_length=64, widget=forms.PasswordInput)