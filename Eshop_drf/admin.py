from django.contrib import admin
from .models import Customer, Vendor, Product, Purchase, Sales


admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Sales)


