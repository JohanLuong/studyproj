from django.shortcuts import render
from datetime import datetime
import requests
import json
# Create your views here.

def GetPrice(request):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    rawdata = response.json()
    result = {'result': rawdata}
    return render(request, 'home.html', result)