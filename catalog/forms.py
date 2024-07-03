from django.forms import ModelForm, forms, BooleanField

from .models import Product, Version


class StyleFormMixin:
    """ Миксин для формы стилей. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
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


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
