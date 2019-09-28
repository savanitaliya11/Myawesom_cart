# shop/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    allProds = []
    catprods = Product.objects.values('product_desc', 'id')
    cats = {item['product_desc'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_desc=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


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
