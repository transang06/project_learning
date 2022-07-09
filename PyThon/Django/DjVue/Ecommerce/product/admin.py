from product.models import Product,ProductPhoto
from django.contrib import admin

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','amount','description')
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at')
# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto,PhotoAdmin)
