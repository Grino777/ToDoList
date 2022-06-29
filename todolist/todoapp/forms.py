from django import forms
from .models import UserModel

class UserForms(forms.ModelForm):
    class Meta:
        model = UserModel
        password = forms.CharField(widget=
        })