from django.contrib import admin
from .models import Category, Brand, Product, CartItem, Cart, Order, Payment

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['Product', 'quantity', 'cost']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'items', 'total_cost']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'status', 'code']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'user', 'amount', 'refrence_id', 'status', 'time']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'category', 'brand', 'price', 'quantity', 'uploaded_at' )
    list_filter = ('category', 'brand', 'price', 'uploaded_at')
    search_fields = ('name', 'brand', 'category', )
    readonly_fields = ('id', 'uploaded_at' )


admin.site.register( Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
# Register your models here.