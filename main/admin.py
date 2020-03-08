from django.contrib import admin
from .models import Watch, Brand, Store, Price
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ['cleaned_name']

class WatchAdmin(admin.ModelAdmin):
    readonly_fields = ['cleaned_reference']

admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Store, BrandAdmin)
admin.site.register(Price)
