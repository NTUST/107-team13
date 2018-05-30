from django.contrib import admin

# Register your models here.
from .models import Member,Seller,Buyer

admin.site.register(Member)
admin.site.register(Seller)
admin.site.register(Buyer)