from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

#from django.template.context_processors import csrf
#from django.views.decorators.csrf import csrf_protect

from django.views.decorators.csrf import csrf_exempt

@require_POST
#@csrf_protect # <------
@csrf_exempt # <------
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartDetail')


# Нам также нужна возможность удалять товары, давайте добавим в views.py следующий код:

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


#Теперь когда мы создали две функции для добавления и удаления 
#товаров из корзины, настала пора создать вьюху для отображения 
#корзины. Добавим в наш views.py код:

# Эта функция получает экземпляр корзины пользователя и 
# передает его в качестве параметра в шаблон.

def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'cart/detail.html', {'cart': cart})
