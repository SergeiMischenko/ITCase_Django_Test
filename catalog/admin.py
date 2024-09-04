from django.contrib import admin

from catalog.models import ProductImage, ProductParameter, Product


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "base_price", "sort_order")
    inlines = [ProductImageInline, ProductParameterInline]
    search_fields = ["name"]
    ordering = ["sort_order"]
