from django.contrib import admin

from .models import Category, Product, ProductImages, PrincipalProduct



class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    
admin.site.register(Category, CategoryAdmin)




class ProductImageAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    inlines = [ProductImageAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(PrincipalProduct)

