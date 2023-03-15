from django.contrib import admin
from .models import *

admin.site.register([Category,Furniture,Order,OrderItem,Customer,ShippingAddress])

