from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group 
#to remove the model 'group from amin panel, import group as shown then unregister using the following line of code as shown below


admin.site.site_header = 'Inventory MS Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)  # use this to remove/unregister groups from admin panel

