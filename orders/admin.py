from django.contrib import admin
from .models import Order, Customer, Part, Item

# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Part)
admin.site.register(Item)