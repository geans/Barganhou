from django.contrib import admin
from .models import ProductInfo

class ProductInfoAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'local', 'date_log')

admin.site.register(ProductInfo, ProductInfoAdmin)
