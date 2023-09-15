from django.contrib import admin
from .models import Category, Product, Client, Order
from .forms import ProductForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['name', 'slug', 'description', 'price', 'available', 'created', 'updated', ]
    list_filter = ['name', 'available', 'created', 'updated', ]
    list_editable = ['price', 'available',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    list_filter = ['name', 'address', 'phone']
    list_editable = ['address']
    list_display_links = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']