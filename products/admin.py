from django.contrib import admin
from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'active', 'price')

