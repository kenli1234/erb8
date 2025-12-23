from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
#    return HttpResponse("<h1>Hello World</h1>")
    print(request, request.path)
    return render(request, 'pages/index.html')

def about(request):
    print(request, request.path)
    return render(request, 'pages/about.html')
#    return HttpResponse("<h1>about</h1>")