from .models import Drug

from django import forms


class DrugCreation(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'price', 'stock']
