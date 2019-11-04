from django import forms
from django.utils.translation import gettext as _


class UserLoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
