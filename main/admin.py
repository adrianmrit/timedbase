from django.contrib import admin
from .models import Watch, Brand
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ['cleaned_name']

class WatchAdmin(admin.ModelAdmin):
    readonly_fields = ['cleaned_reference']

admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)
