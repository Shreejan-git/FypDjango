from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=[
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title=forms.CharField()
    description=forms.CharField()
    price= forms.DecimalField()

class DiabetesForm(forms.Form):
    pregnancy=forms.FloatField()
    glucose=forms.FloatField()
    blood_pressure=forms.FloatField()
    skin_thickness=forms.FloatField()
    insulin=forms.FloatField()
    bmi=forms.FloatField()
    diabetes_pedigree_fucntion=forms.FloatField()
    age=forms.FloatField()

class HomeForm(forms.Form):
    post = forms.CharField()