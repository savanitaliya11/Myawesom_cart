# shop/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    p = Product.objects.all()
    print(p)
    n = len(p)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # consider n=4 then,n//4 = 1 + ceil((n/4 = 1)-(n//4 = 1)) = 0 then no. of slides is 1
    # consider n=5 n//5 = 1.25 consider(1) + ceil((1.25)-(1)) = 1.25 consider (2 because 1.25
    # is o/p of ceil)then oyr no. of slides is 2
    dict = {'no.of slides': nSlides, 'range': (1, nSlides), 'product': p}
    return render(request, 'shop/index.html', dict)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Hey there,this is contact")


def tracker(request):
    return HttpResponse("Hey there,this is tracker")


def search(request):
    return HttpResponse("Hey there,this is search")


def productview(request):
    return HttpResponse("Hey there,this is p-view")


def checkout(request):
    return HttpResponse("Hey there,this is checkout")
