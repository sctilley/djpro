from django.shortcuts import render
from django.http import HttpResponse

def tracker(request):
    return render(request, 'tracker/about.html', {'title': 'MTGO Leage Tracker'})
