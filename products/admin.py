from django.contrib import admin
from .models import Category,Product,File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['titles']

class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_enable']
    list_display = ['title','is_enable','created_time']
    search_fields = ['title']
    filter_horizontal = ['categoreis']
    inlines = [FileInLineAdmin]