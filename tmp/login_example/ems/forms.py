from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'description', 'price', 'quantity' ]

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    #your_name = forms.CharField(label='Your Name', max_length=100, widget=forms.Textarea)

