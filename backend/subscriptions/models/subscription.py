from django.db import models
from django.core import validators

class Subscription(models.Model):
    # properties
    email = models.EmailField(max_length = 254, validators=[validators.validate_email])
    stock_ticker = models.CharField(max_length=200, null=False)
