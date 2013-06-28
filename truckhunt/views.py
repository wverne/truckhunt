from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from django.template import Context
from django.http import *
from django.contrib.auth import authenticate, login, logout

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

    return render(request, 'truck_page.html',
                  {'trucks_list': FoodTruck.objects.all(),
                   'this_truck':  truck_object[0]})

def featured_page(request):
    return render(request, 'featured.html', {})

def about_page(request):
    return render(request, 'about.html', {})

def map_test_page(request):
    return render(request, 'map_test.html',
                  {'trucks_list': FoodTruck.objects.all()})

def login_view(request):
    if not 'username' in request.POST:
        return redirect('/invalid_login/')
    if not 'password' in request.POST:
        return redirect('/invalid_login/')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/disabled_account/')
    return redirect('/invalid_login/')

def logout_view(request):
    logout(request)
    return redirect('/')

def disabled_page(request):
    return render(request, 'disabled_account.html', {})

def invalid_login_page(request):
    return render(request, 'invalid_login.html', {})

def user_page(request, inusername):
    # find appropriate user
    user_object = User.objects.filter(username=inusername)
    if not user_object:
        raise Http404

    return render(request, 'user_page.html',
                  {'this_user':  user_object[0]})
