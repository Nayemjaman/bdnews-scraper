from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("<h1><a href="">Go here!</a></h1></br> <h3>User name : dailystar </h3> </br> <h4>Password : daily@star<h4>")