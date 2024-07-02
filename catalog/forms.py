from django.forms import ModelForm, forms

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')

    def clean_title(self):
        """ Проверка на запрещенное название. """
        ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']
        title = self.cleaned_data.get('title')
        if title.lower() in ban_list:
            raise forms.ValidationError('Запрещенное название!')
        return title
