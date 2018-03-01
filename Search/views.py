from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from CheckPrice.models import PriceDB
from datetime import datetime
from . import form
# Create your views here.

def SearchForm(request):
    return render(request, "search-form.html")

def Search(request):
    if "key" in request.GET and request.GET["key"]:
        #message = "You have searched for {}.".format(request.GET["key"])
        keyword = request.GET["key"]
        result = PriceDB.objects.filter(name=keyword)
        return render(request, "result.html", {"result": result ,"key": request.GET["key"], "moment": datetime.now()})
    else:
        message = "Not Found!"
    return HttpResponse(message)