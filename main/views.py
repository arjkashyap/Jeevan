from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from drawnow import *

def makeFig():
    ax1 = plt.subplot(211)
    plt.ylim(0,50)
    plt.title('Flowrate')
    plt.grid(True)
    plt.ylabel('Flow')
    plt.plot(f, 'ro-', label='litre/min')
    plt.legend(loc='upper left')
    
    


    ax2 = plt.subplot(212, sharex=ax1)
    plt.ylim(0,10000)
    
    plt.grid(True)
    plt.ylabel('volume')
    plt.plot(v, 'ro-', label='mL')
    plt.legend(loc='upper left')

def vol():
    ser = serial.Serial('COM4', baudrate = 9600)
    a = []
    t_end = time.time() + 10 #########
    while time.time() < t_end:
        arduinoData = ser.readline().decode('ascii')
        a.append(arduinoData)
        print(arduinoData)
    #return a[-1]
    for i in range(0,len(a)):
        pos1 = a[i].find(", ")
        #print(pos)
        pos2 = a[i].find("\r")
        a[i] =  a[i][pos1+2:pos2]
    print(a)
    a = [int(i) for i in a]
    return a
        



@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/index.html')

@login_required
def emarket(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    emarket = Emarket.objects.all().exclude(verify = False)
    pos = Emarket.objects.values_list('latt', 'lonn')
    a = np.array(pos)
    lat1=[]
    long1=[]
    for i in range(len(a)):
        lat1.append(a[i][0])
        long1.append(a[i][1])
    return render(request, 'main/emarket.html', {"emarket": emarket ,'lat' : lat1 , 'lng':long1 })


class AddShop(CreateView):
    model = Emarket
    fields = ['name', 'owner', 'city_location', 'description', 'logo', 'latt', 'lonn']
    template_name = "main/shop_form.html"

def location(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    em = Emarket.objects.all().exclude(verify = False)
    pos = Emarket.objects.values_list('latt', 'lonn')

    a = np.array(pos)
    lat1=[]
    long1=[]
    for i in range(len(a)):
        lat1.append(a[i][0])
        long1.append(a[i][1])
    return render(request, 'main/location.html', {"em": em ,'lat' : lat1 , 'lng':long1 })

@login_required
def details(request, incubator_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    em = get_object_or_404(Emarket, pk = incubator_id)
    details = Details.objects.get(pk = incubator_id)
    return render(request, 'main/details.html', {'em': em, 'details': details})

@login_required
def added(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/added.html', context = None)

@login_required 
def result(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    # Shows the matched result
    query = request.GET.get('em_search')
    check = Emarket.objects.filter(name__icontains= query).exclude(verify = False)
    return render(request, 'main/results.html', {'check': check})

@login_required 
def footprint(request):
    v  = vol()
    volume = v
    return render(request, 'main/footprint.html', {'volume': volume})

@login_required 
def data(request):
    return render(request, 'main/data.html', context = None)

@login_required
def join(request):
    drives = Plantation.objects.all()
    return render(request, 'main/join.html', {'drives': drives})

class Add(CreateView):
    model = Plantation
    fields = ['name', 'city', 'date', 'contact', 'description']
    template_name = "main/join_form.html"

def discover(request):
    return render(request, 'main/discover.html', context = None)

def disc_details(request):
    return render(request, 'main/discDetails.html', context = None)


class AddDiscover(CreateView):
    model = Discover
    fields = ['name', 'image', 'location', 'description']
    template_name = "main/addDiscover_form.html"
"""


def disc_details(request, discover_id):
    print(discover_id )
    dis = get_object_or_404(Discover, pk = discover_id)
    det = DiscDetails.objects.get(pk = discover_id)
    
    return render(request, 'main/discDetails.html', {'det': det, 'dis': dis})
"""
class ContactForm(CreateView):
    model = Join
    fields = ['name', 'contact', 'email']
    template_name = "main/contact_form.html"