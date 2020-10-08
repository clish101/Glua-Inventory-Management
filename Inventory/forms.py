from .models import Drug
from django.db import models
from django import forms


class DrugCreation(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'buying_price','maximum_price', 'stock']

