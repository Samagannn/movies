from django.contrib import admin
from .models import Product, ProductImage, ProductAttribute
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]

    list_display = ('id', 'title', 'price', 'category', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content')
    list_filter = ('category', 'tags')

    def get_image(self, obj):
        if obj.images.exists():
            image_url = obj.images.first().image.url
            return format_html('<img src="{}" height="50">', image_url)
        return None

    get_image.short_description = 'Изображение'


admin.site.register(ProductAttribute)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'get_image')
    list_display_links = ('id', 'product')
    search_fields = ('id', 'product')

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50">', obj.image.url)
        return None

    get_image.short_description = 'Изображение'


# Register your models here.
