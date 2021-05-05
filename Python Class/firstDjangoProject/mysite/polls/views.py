from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, fellow pythonistas in Zuri. Nice to meet everyone of you")

