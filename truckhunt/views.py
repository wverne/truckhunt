from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from gmapi import maps
from truckhunt.forms import *

def homepage(request):
    return render(request, 'homepage.html', {})

def trucks_page(request):
    return render(request, 'trucks.html', {})

def types_page(request):
    return render(request, 'types.html', {})

def featured_page(request):
    return render(request, 'featured.html', {})

def map_test_page(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(38, -97),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    context = {'gmapform': MapForm(initial={'map': gmap})}
    return render_to_response('map_test.html', context)
