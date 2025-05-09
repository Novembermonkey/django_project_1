from django import forms

from shop.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at', 'product')