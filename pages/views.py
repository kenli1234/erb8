from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from doctors.models import Doctor
from listings.choices import district_choices, room_choices, rooms_choices

# ! Create your views here.
# TODO: update index and about views
# # Homepage
# ? List 3 latest listings
# * dafwrgtrwdasfgeg
def index(request):
#    return HttpResponse("<h1>Hello World</h1>")
#    print(request, request.path)
#    return render(request, 'pages/index.html')
#    return render(request, 'pages/index.html',{'anything':'something', 'number':1234})

    #print('TEST*************AAAAA')
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #context = {"listings": listings}
    #print('TEST*************', listings)
    context = {"listings": listings,
               "district_choices": district_choices, 
               "room_choices": room_choices, 
               "rooms_choices": rooms_choices}
    return render(request, 'pages/index.html', context)

def about(request):
    #print('TEST*************!!!')
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
    context = {"doctors": doctors,
               "mvp_doctors": mvp_doctors}


    #print('***************mvp_doctors:********:', len(mvp_doctors))


    #print(request, request.path)
    return render(request, 'pages/about.html', context)
#    return HttpResponse("<h1>about</h1>")