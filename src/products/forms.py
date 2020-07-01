from django import forms

from .models import Productshree

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productshree
        fields=[
            'title',
            'description',
            'price'

        ]

class RawProductForm(forms.Form):
    title= forms.CharField()
    description= forms.CharField()
    price = forms.DecimalField()


