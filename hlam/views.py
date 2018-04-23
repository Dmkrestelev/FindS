from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    latest_question_list = Users.objects[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)