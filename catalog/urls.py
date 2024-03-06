from django.urls import path, include

from catalog.views import homepage, contactspage

urlpatterns = [
    path('', homepage),
    path('', contactspage)
]
