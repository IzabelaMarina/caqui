from django import forms

class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class PasswordModelField(forms.CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)

class FormLoginUser(forms.Form):

    login = forms.CharField(label='Login')
    password = PasswordModelField()