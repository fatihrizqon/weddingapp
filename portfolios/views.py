from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title' : 'Dalmore Planner',
        'meta'  : 'Meta Description',
    }
    return render(request, 'portfolios/index.html', context)
