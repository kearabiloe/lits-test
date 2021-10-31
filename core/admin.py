from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('avatar',)}),
    )



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["__str__","quantity","total"]
    search_fields = ["material",'material__vendor']
    list_filter = ["material__name","material__vendor__name"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__","total"]
    raw_id_fields = ("items",)
    readonly_fields = ('placed_date',)

# Re-register UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(Material)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)
