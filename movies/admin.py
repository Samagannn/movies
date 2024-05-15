from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.utils.html import format_html


@admin.register(Profile)
@admin.register(Log)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]

    list_display = ('id', 'title', 'price', 'category', 'author', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content')
    list_filter = ('category', 'tags', 'author')

    def get_image(self, obj):
        image = obj.images.first()
        if image and image.image:
            return format_html('<img src="{}" height="50">', image.image.url)
        return None

    get_image.short_description = 'Изображение'


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


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')
    search_fields = ('id', 'product')

# Register your models here.
