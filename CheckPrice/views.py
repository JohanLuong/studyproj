from django.shortcuts import render
from datetime import datetime
from CheckPrice.models import PriceDB
import requests
import json
# Create your views here.

def GetPrice(request):
    #Fetch data from third pary API
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    rawdata = response.json()

    #Insert data
    for i in range(len(rawdata)):
        insert_data = PriceDB(coinid=rawdata[i]["id"],
                              name=rawdata[i]["name"],
                              symbol=rawdata[i]["symbol"],
                              rank=rawdata[i]["rank"],
                              price_usd=rawdata[i]["price_usd"],
                              price_btc=rawdata[i]["price_btc"],
                              volume_24h=rawdata[i]["24h_volume_usd"],
                              market_cap=rawdata[i]["market_cap_usd"],
                              available_supply=rawdata[i]["available_supply"],
                              total_supply=rawdata[i]["total_supply"],
                              max_supply=rawdata[i]["max_supply"],
                              percent_change_1h=rawdata[i]["percent_change_1h"],
                              percent_change_24h=rawdata[i]["percent_change_24h"],
                              percent_change_7h=rawdata[i]["percent_change_7d"],
                              last_update=rawdata[i]["last_updated"])
        insert_data.save()

    #result = {'result': rawdata}
    result = PriceDB.objects.all()
    return render(request, 'home.html', {"result": result})