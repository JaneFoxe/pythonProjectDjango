from django.conf import settings
from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cached_categories():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_name'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)

    return categories
