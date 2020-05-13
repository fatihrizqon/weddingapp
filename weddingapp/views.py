from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    context = {
        'title' : 'Dalmore Planner - Home Page',
        'meta'  : 'Meta Description',
    }
    return render(request, 'index.html', context)
