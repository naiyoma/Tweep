from django.shortcuts import render

from django.http import HttpResponse


from .models import User

# Create your views here.


def index(request):
    # index
    output = "hello world"
    return HttpResponse(output)
