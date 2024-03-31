from django.urls import path

from catalog.views import homepage, contactspage, product_card
from catalog.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', homepage, name='home'),
    path('contacts/', contactspage, name='contacts'),
    path('<int:pk>/', product_card, name='product_card')
]
