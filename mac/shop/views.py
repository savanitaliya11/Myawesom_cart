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


def contact(request):
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request):
    return render(request, 'shop/productview.html')


def checkout(request):
    return HttpResponse("Hey there,this is checkout")
