from django.contrib import admin
from .models import Order, Product, UUser, Buy

admin.site.site_header = 'Админ раздел'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(UUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    pass
