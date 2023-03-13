from django.contrib import admin
from . models import *

class AdminCart(admin.ModelAdmin):
    list_display = ['pd', 'qty', 'price']
    fields = ['pd', 'qty']
admin.site.register(Cart, AdminCart)

class adminCateg(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Categories, adminCateg)

class adminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'availability']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(product, adminProduct)


