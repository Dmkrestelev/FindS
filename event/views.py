from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models

def index(request):
    create_model()


def create_model(self):
    check_save = models.Event.objects.all()

    return HttpResponse(check_save)
