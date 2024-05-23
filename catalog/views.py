from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_cached_categories


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(name=product)
            active_versions = versions.filter(version_now=True)
            if active_versions:
                product.active_version = active_versions.last().version_name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data

class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_cached_categories()

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        versions = Version.objects.filter(name=product)
        active_versions = versions.filter(version_now=True)
        if active_versions.exists():
            product.active_version = active_versions.first().version_name
        else:
            product.active_version = 'Нет активной версии'

        # if settings.CACHE_ENABLED:
        #     key = f'category_name_{self.object.pk}'
        #     category_name = cache.get(key)
        #     if category_name is None:
        #         category_name = self.object.category
        #         cache.set(key, category_name)
        #     else:
        #         category_name = self.object.category

        context['version'] = product.active_version
        context['version_list'] = versions
        # context['subjects'] = category_name

        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Product
    form_class = ProductForm
    # permission_required = 'users.change_product'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            product = form.save(commit=False)  # Сохраняем форму без коммита
            user = self.request.user
            product.owner = user
            product.save()  # Сохраняем продукт с установленным владельцем
            formset.instance = product
            formset.save()  # Сохраняем формсет
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.set_published') and user.has_perm('catalog.change_description') and user.has_perm(
                'catalog.change_category'):
            return ModeratorForm
        raise PermissionDenied
