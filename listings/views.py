from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from django.core.paginator import Paginator

# Create your views here.
def listings(request):
#    return HttpResponse("<h1>Hello World</h1>")
    #print(request, request.path)
    #print('aaaaaaaaaa')
    #print('listings', len(listings))

    listings = Listing.objects.filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {"listings": paged_listings}
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
#    print(request, request.path)
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, 'listings/listing.html', context)
#    return HttpResponse("<h1>about</h1>")

def search(request):
    print(request, request.path)
    return render(request, 'listings/search.html')
#    return HttpResponse("<h1>about</h1>")