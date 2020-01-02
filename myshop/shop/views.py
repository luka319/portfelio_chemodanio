from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from cart.forms import CartAddProductForm  # part 4

# Страница с товарами
def ProductList(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара

"""  !!! old from part 3
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

    # !!! old from part 3
"""

from django.shortcuts import render_to_response

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render_to_response('shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})

#===================================================
