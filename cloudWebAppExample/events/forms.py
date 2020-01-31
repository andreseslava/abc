from django import forms
from django.forms import SelectDateWidget


class EventsForm(forms.Form):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del evento'}))
    address = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}))
    place = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar'}))
    description = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    startDate = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), ), )
    endDate = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), ), )


