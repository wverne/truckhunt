from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import *
from gmapi import maps
from truckhunt.forms import *
from foodtrucks.models import *

def homepage(request):
    return render(request, 'homepage.html', 
                  {'trucks_list': FoodTruck.objects.all()})

def trucks_page(request, truckname=""):
    if (truckname==""):
        return render(request, 'trucks.html',
                      {'trucks_list': FoodTruck.objects.all()})

    # find appropriate truck
    truck_object = FoodTruck.objects.filter(name=truckname)
    if not truck_object:
        raise Http404

    return render(request, 'trucks.html',
                  {'trucks_list': truck_object})

def types_page(request):
    return render(request, 'types.html', {})

def featured_page(request):
    return render(request, 'featured.html', {})

def map_test_page(request):
    return render(request, 'map_test.html',
                  {'trucks_list': FoodTruck.objects.all()})
