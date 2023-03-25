from django.contrib import admin

from .models import Category, Product, ProductImages, PrincipalProduct



class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'name', 'created', 'image', 'slug')
    search_fields = ('name',)
    ordering = ('id',)
    
admin.site.register(Category, CategoryAdmin)




class ProductImageAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'name', 'description', 'price', 'principal_image', 'created', 'slug')
    ordering = ('-created',)
    search_fields = ('name',)
    inlines = [ProductImageAdmin]
    

admin.site.register(Product, ProductAdmin)
admin.site.register(PrincipalProduct)

