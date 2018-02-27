from django.db import models

# Create your models here.
class PriceDB(models.Model):
    coinid = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=25, blank=False, null=False)
    symbol = models.CharField(max_length=5, blank=False, null=False)
    rank = models.IntegerField()
    price_usd = models.FloatField()
    price_btc = models.FloatField()
    volume_24h = models.FloatField()
    market_cap = models.FloatField()
    available_supply = models.FloatField()
    total_supply = models.FloatField()
    max_supply = models.FloatField(blank=True, null=True)
    percent_change_1h = models.FloatField()
    percent_change_24h = models.FloatField()
    percent_change_7h = models.FloatField()
    last_update = models.CharField(max_length=25)