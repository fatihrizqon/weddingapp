from django.shortcuts import render
from django.http import HttpResponse
from packages.models import Package
from django.db.models import Q

def index(request):
    data = Package.objects.all()
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
        'data'    : data
    }
    return render(request, 'pricing/index.html', context)

