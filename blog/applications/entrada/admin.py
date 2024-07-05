from django.contrib import admin
#
from .models import Entry, Tag, Category
# Register your models here.


class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'category',
        #'tag',
        'title',
        'resume',
        'content',
        'public',
        'image',
        'portada',
        'in_home',
    )

admin.site.register(Entry, EntryAdmin)



class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


admin.site.register(Tag, TagAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)