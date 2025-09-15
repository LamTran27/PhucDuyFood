from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html

from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'image_preview', 'price', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" />', obj.image.url)
        return "Không có ảnh"
    image_preview.short_description = "Ảnh sản phẩm"

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)

   