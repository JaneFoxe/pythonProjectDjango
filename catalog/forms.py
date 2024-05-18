from django import forms
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class StyleMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ModeratorForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
