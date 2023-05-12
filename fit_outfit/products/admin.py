from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'category',
        'description',
        'price',
        'size'
    )
    list_editable = ('category',)
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
