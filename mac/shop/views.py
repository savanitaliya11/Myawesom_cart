# shop/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
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

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("Hey there,this is checkout")
