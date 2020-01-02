from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Order, OrderItem


from django.urls import reverse # new

def OrderDetail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))
OrderDetail.short_description = 'Инфо'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated',
                   ]
                   # OrderDetail]

    list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemInline]

    # list_editable = ['first_name', 'last_name', 'email']
    # prepopulated_fields = {'slug': ('first_name', )}


admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemInline)

"""
============

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

"""
