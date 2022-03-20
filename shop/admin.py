from django.contrib import admin
from .models import Order, Product, UUser
admin.site.site_header = 'Админ раздел'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(UUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'username', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
