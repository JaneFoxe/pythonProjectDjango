from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def homepage(request):
    return render(request, 'catalog/home.html')


def contactspage(request):
    return render(request, 'catalog/contacts.html')
