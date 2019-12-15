# Register your models here.
from django.contrib import admin

from .models import Blog, Label, Status


class LabelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 10


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ['status', 'modify_date', 'label']
    ordering = ['-modify_date']
    search_fields = ['title']
    list_per_page = 10


admin.site.register(Label, LabelAdmin)
admin.site.register(Blog, BlogAdmin)
#admin.site.register(Status)
