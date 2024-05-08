from django.shortcuts import render


def index(request):
    return render(request, "home.html")


def shop(request):
    return render(request, 'shop.html')


def products(request):
    return render(request, 'products.html')


def personal(request):
    return render(request, 'personal.html')


def imprint(request):
    return render(request, 'imprint.html')
