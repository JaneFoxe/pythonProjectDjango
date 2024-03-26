from django.urls import path, include

from catalog.views import homepage, contactspage, product_card
from catalog.apps import MainappConfig

app_name = MainappConfig.name



urlpatterns = [
    path('', homepage,),
    path('contacts/', contactspage),
    path('<int:pk>/', product_card, name='product_card')
]
