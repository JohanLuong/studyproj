from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from CheckPrice.models import PriceDB
# Create your views here.

def SearchForm(request):
    return render(request, "search-form.html")

def Search(request):
    if "keyword" in request.GET:
        message = "You have searched for {}.".format(request.GET["keyword"])
    else:
        message = "Not Found!"
    return HttpResponse(message)