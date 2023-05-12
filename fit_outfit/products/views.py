from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, CategoryForm
from .models import Product, Category
from .utils import paginate


@login_required
def index(request):
    """Все товары."""
    return render(
        request, 'products/index.html',
        {'page_obj': paginate(request, Product.objects.all())}
    )


@login_required
def categories(request):
    """Все категории."""
    return render(
        request, 'products/categories.html',
        {'page_obj': paginate(request, Category.objects.all())}
    )


@login_required
def category_products(request, slug):
    """Товары категории."""
    return render(
        request, 'products/category_list.html', {
            'page_obj': paginate(
                request, get_object_or_404(Category, slug=slug).products.all()
            ),
            'category': get_object_or_404(Category, slug=slug)
        }
    )


@login_required
def product_create(request):
    """Добавление товара."""
    form = ProductForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, 'products/create_product.html', {'form': form})
    form.save()
    return redirect('products:index')


@login_required
def category_create(request):
    """Добавление категории."""
    form = CategoryForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'products/create_product.html', {'form': form})
    form.save()
    return redirect('products:index')


@login_required
def product_edit(request, product_id):
    """Редактирование товара."""
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None)
    if not form.is_valid():
        form = ProductForm(instance=product)
        is_edit = 'is_edit'
        context = {
            'form': form,
            'product': product,
            'is_edit': is_edit
        }
        return render(request, 'products/create_product.html', context)
    form = ProductForm(request.POST, files=request.FILES or None,
                       instance=product)
    form.save()
    return redirect('products:index')


@login_required
def product_detail(request, product_id):
    """Подробности товара."""
    return render(
        request, 'products/product_detail.html', {
            'product': get_object_or_404(Product, pk=product_id),
        })


@login_required
def product_delete(request, product_id):
    """Подробности товара."""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return render(request, 'products/product_delete.html')


@login_required
def product_quantity(request, product_id, field, sign):
    '''Увеличение или уменьшение количества товара.'''
    product = get_object_or_404(Product, id=product_id)
    if sign == '1':
        if field == '1':
            product.size_s += 1
        elif field == '2':
            product.size_m += 1
        elif field == '3':
            product.size_l += 1
        elif field == '4':
            product.size_xl += 1
        elif field == '5':
            product.size_xxl += 1
        elif field == '6':
            product.size_xxxl += 1
        else:
            product.amount += 1
    elif sign == '2':
        if field == '1':
            product.size_s -= 1
        elif field == '2':
            product.size_m -= 1
        elif field == '3':
            product.size_l -= 1
        elif field == '4':
            product.size_xl -= 1
        elif field == '5':
            product.size_xxl -= 1
        elif field == '6':
            product.size_xxxl -= 1
        else:
            product.amount -= 1
    product.save()
    return redirect('products:product_detail', product_id=product_id)
