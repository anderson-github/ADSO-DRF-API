from django.contrib import admin
from .models import Products, UsersProducts


class UsersProductsAdmin(admin.ModelAdmin):
    model = UsersProducts
    list_display = "__all__"
    list_display_links = "__all__"

# Register your models here.
admin.site.register(Products)
admin.site.register(UsersProducts)

