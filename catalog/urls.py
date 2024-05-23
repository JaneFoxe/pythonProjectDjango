from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView
from catalog.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
