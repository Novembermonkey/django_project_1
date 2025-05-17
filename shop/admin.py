from django.contrib import admin
from .models import Product, Category, Order, Comment
from django.contrib.auth.models import User, Group
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

# admin.site.register(Product)
admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['my_order']
    list_display = ['name', 'price', 'discount', 'category', 'created_at', 'my_order']
    search_fields = ['name']
    list_filter = ['price']


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Online Shop'
admin.site.site_title = 'JS'
admin.site.index_title = "Welcome to online shop"


@admin.register(Comment)
class CommentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'email', 'rating', 'created_at', 'product', 'my_order']


class ProductInline(admin.StackedInline):
    model = Product
    extra = 3

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['title', 'created_at', 'my_order']
