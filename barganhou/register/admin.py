from django.contrib import admin
from .models import ProductInfo, LocalInfo

class ProductInline (admin.TabularInline):
    model = ProductInfo
    extra = 10

class ProductInfoAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'local', 'date_log')

class LocalInfoAdmin (admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(LocalInfo, LocalInfoAdmin)
