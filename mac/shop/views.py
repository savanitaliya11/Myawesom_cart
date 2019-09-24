# shop/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("Hey there,this is about")


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
