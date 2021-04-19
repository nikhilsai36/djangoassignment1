from .models import studentdata
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm

class studentForm(forms.ModelForm):
    class Meta:
        model = studentdata
        fields = "__all__"


class RegistartionForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}))
    gender = forms.ChoiceField(choices=studentdata.GenderChoices, required=False)
    country = forms.ChoiceField(choices=studentdata.country_choices, required=False)
