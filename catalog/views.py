from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def homepage(request):
    return render(request, 'catalog/home.html')


def contactspage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')
    return render(request, 'contacts/contacts.html')

