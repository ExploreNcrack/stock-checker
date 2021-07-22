from django.db import models

class Stock(models.Model):
    # properties
    ticker = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=19, decimal_places=2)
