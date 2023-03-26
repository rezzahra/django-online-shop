from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment

class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('auther', 'body', 'active')
    extra = 1

@admin.register(Product)
class AdminProduct(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'active', 'price')
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('auther', 'body', 'active')
