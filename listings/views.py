from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listings(request):
#    return HttpResponse("<h1>Hello World</h1>")
    print(request, request.path)
    return render(request, 'listings/listings.html')

def listing(request, listing_id):
    print(request, request.path)
    return render(request, 'listings/listing.html')
#    return HttpResponse("<h1>about</h1>")

def search(request):
    print(request, request.path)
    return render(request, 'listings/search.html')
#    return HttpResponse("<h1>about</h1>")