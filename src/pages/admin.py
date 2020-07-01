from django.contrib import admin

# Register your models here.
from .models import Product, Sales, Shree
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(Shree)