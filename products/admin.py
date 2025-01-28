from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category,Product,File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['titles']

class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable','file_type']
    extra = 0

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter = ['is_enable']
    list_display = ['title','is_enable','created_time']
    search_fields = ['title']
    filter_horizontal = ['categoreis']
    inlines = [FileInLineAdmin]