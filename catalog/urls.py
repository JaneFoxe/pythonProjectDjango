from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactsView
from catalog.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_card')
]
