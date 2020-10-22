from .models import Drug
from django.db import models
from django import forms


class DrugCreation(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'category', 'buying_price','minimum_price','ref_code', 'maximum_price', 'stock']
