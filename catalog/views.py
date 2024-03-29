from django.shortcuts import render
from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def homepage(request):
    card = Product.objects.all()
    context = {
        "object_list": card
    }
    return render(request, 'catalog/home.html', context)


def contactspage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product_card(request, pk):
    card = Product.objects.get(pk=pk)
    context = {
        "object": card
    }
    return render(request, 'catalog/product_card.html', context)
