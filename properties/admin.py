from django.contrib import admin
from .models import BuyProperty, Category
# Register your models here.

#property
admin.site.register(BuyProperty)
#category
admin.site.register(Category)