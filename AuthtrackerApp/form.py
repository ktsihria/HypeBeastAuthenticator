from django import forms
from AuthtrackerApp.models import Barcode

class Barcode(forms.Form):
    barcode = forms.CharField()
