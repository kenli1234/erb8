from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.
def index(request):
#    return HttpResponse("<h1>Hello World</h1>")
#    print(request, request.path)
#    return render(request, 'pages/index.html')
#    return render(request, 'pages/index.html',{'anything':'something', 'number':1234})

    print('TEST*************AAAAA')
    listings = Listing.objects.all()
    context = {"listings": listings}
    print('TEST*************', listings)
    return render(request, 'pages/index.html', {"listings": listings})

def about(request):
    print('TEST*************!!!')
    print(request, request.path)
    return render(request, 'pages/about.html')
#    return HttpResponse("<h1>about</h1>")