from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting


# Create your views here.
def date(request):
    return HttpResponse("Index page serve at  " + str(datetime.now()))


def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})


def about(request):
    return HttpResponse("We are learning python")
