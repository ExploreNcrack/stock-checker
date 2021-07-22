from django import forms
from django.forms import widgets
from .models import *
from django.core.exceptions import ValidationError
import yfinance as yf

class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    stock_ticker = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))

    class Meta:
        model = Subscription
        fields = ["stock_ticker", "email"]

    def clean_stock_ticker(self):
        data = self.cleaned_data['stock_ticker']
        t = yf.Ticker(data)
        if  len(t.info) <= 2 and not t.info["regularMarketPrice"] and not t.info["logo_url"]:
            raise ValidationError("Invalid stock ticker")
        return data

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        stock_ticker = cleaned_data.get("stock_ticker")
        if Subscription.objects.filter(email=email, stock_ticker=stock_ticker).exists():
            raise ValidationError("This email has subscribed to this stock ticker already")
