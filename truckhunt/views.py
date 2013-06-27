from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from gmapi import maps
from truckhunt.forms import *
from foodtrucks.models import *

def homepage(request):
    return render(request, 'homepage.html', 
                  {'trucks_list': FoodTruck.objects.all()})

def trucks_page(request):
    return render(request, 'trucks.html', {})

def types_page(request):
    return render(request, 'types.html', {})

def featured_page(request):
    return render(request, 'featured.html', {})

def map_test_page(request):
    return render(request, 'map_test.html', {})
