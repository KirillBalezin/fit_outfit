from django import forms

from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'size',
                  'purchase_price', 'price', 'image')
        labels = {
            'title': 'Название товара',
            'category': 'Категория',
            'description': 'Описание',
            'size': 'Размеры',
            'purchase_price': 'Закупочная цена',
            'price': 'Цена',
            'image': 'Изображение'
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'slug', 'description')
        labels = {
            'title': 'Название категории',
            'slug': 'Ссылка',
            'description': 'Описание'
        }


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('size_s', 'size_m', 'size_l', 'size_xl', 'size_xxl',
                  'size_xxxl')
