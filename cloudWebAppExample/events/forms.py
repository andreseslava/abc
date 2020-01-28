from django import forms
from django.forms import SelectDateWidget


class EventsForm(forms.Form):
    fecha = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), ), )
