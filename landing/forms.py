from django import forms
from .models import CustomerLead, Product

class CustomerLeadForm(forms.ModelForm):
    class Meta:
        model = CustomerLead
        fields = ['name', 'email', 'phone']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'image']


