from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
