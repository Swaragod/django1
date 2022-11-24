from django.contrib import admin

# Register your models here.

from phones.models import Phone


@admin.register(Phone)    # vladimir / admin
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'lte_exists']
    prepopulated_fields = {"slug": ("name",)}

