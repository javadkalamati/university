from django import forms
from django.forms import ModelForm
from .models import Person


class StudentCreateForm(forms.Form):
    name=forms.CharField()
    family=forms.CharField()
    mellinumber=forms.CharField()
    address=forms.CharField()
    birthday=forms.DateField()

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=('name','family','mellinumber','address','birthday')
