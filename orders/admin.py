from django.contrib import admin
from .models import Order, Customer, Part, Item

# Register your models here.
admin.register(Order)
admin.register(Customer)
admin.register(Part)
admin.register(Item)