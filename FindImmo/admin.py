from django.contrib import admin
from .models import Category, Product,Project, Vendor,Zone,Localite,TypeProject,Service,TypeService,Commodite

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class CommoditeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Commodite, CommoditeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'localite', 'category', 'price','available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class VendorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal', {'fields': ['name','email','phone1','phone2','phone3']}),
        ('Physical', {'fields': ['address','ville','localization']}),
    ]
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Service)
admin.site.register(TypeService)
admin.site.register(TypeProject)
admin.site.register(Zone)
admin.site.register(Localite)
admin.site.register(Project)
