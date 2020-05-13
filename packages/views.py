from django.shortcuts import render
from django.http import HttpResponse
from .models import Package
from django.db.models import Q

def index(request):
    data = Package.objects.all()
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
        'data'    : data
    }
    return render(request, 'packages/index.html', context)

# Working with limitations
def search(request):
    query    = request.GET.get('q')
    data     = Package.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)| Q(price__icontains=query)
            )
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
        'data'    : data
    }
    return render(request, 'packages/index.html', context)

def view(request,id):
    data = Package.objects.filter(id=id)
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
        'data'  : data
    }
    return render(request, 'packages/view.html', context)

def category(request,venue):
    data = Package.objects.filter(venue__icontains = venue)
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
        'data'  : data
    }
    return render(request, 'packages/index.html', context)