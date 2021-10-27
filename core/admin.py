from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["material","quantity","total"]
    search_fields = ["material",'material__vendor']
    list_filter = ["material__name","material__vendor__name"]

admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(Material)
admin.site.register(OrderItem,OrderItemAdmin)
