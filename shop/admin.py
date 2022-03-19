from django.contrib import admin
from .models import Order, User, Product

admin.site.site_header = 'Админ раздел'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
