from django import forms

class FormLoginUser(forms.Form):

    login = forms.CharField(max_length=42,label='Usuário')
    password = password = forms.CharField(max_length=64, widget=forms.PasswordInput,label='Senha')