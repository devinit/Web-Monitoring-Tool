from django import forms
from django.utils.translation import gettext as _

from account.usecases import UserLogin


class UserLoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
