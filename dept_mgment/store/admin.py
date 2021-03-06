from django.contrib import admin

from .models import (Bill, Category, Jobtype, Order, Product, ProductSale,
                     Rack, Staff, Status, Supplier)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'stock', 'cost_price', 'sell_price',
                    'category', 'supplier', 'mfd_date', 'exp_date', 'rack')
# # Register your models here.
admin.site.register(Bill)
admin.site.register(ProductSale)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Jobtype)
admin.site.register(Order)
admin.site.register(Rack)
admin.site.register(Staff)
admin.site.register(Status)
