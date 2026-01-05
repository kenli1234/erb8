from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from django.core.paginator import Paginator
from listings.choices import district_choices, room_choices, rooms_choices
from django.db.models import Q

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
    #print(request, request.path)
    queryset_list = Listing.objects.order_by("-list_date")
    if 'keywords' in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(doctor__name__icontains=keywords))
            print('keywords --', queryset_list)
    if 'district' in request.GET:
        district = request.GET["district"]
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
            print('district --', queryset_list)

    if 'room_type' in request.GET:
        room_type = request.GET["room_type"]
        if room_type:
            queryset_list = queryset_list.filter(room_type__iexact=room_type)
            
    if 'rooms' in request.GET:
        rooms = request.GET["rooms"]
        if rooms:
            queryset_list = queryset_list.filter(rooms__gte=rooms)

    print('*******district**********', request.GET.get('district'))
    print('*******queryset_list**********', len(queryset_list))

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page', 1)
    paged_listings = paginator.get_page(page)

    print('*******paged_listings.has_other_pages**********', paged_listings.has_other_pages)
    
    context = {"listings": paged_listings,
               "district_choices": district_choices, 
               "room_choices": room_choices, 
               "rooms_choices": rooms_choices,
               "values": request.GET}
    return render(request, 'listings/search.html', context)
#    return HttpResponse("<h1>about</h1>")