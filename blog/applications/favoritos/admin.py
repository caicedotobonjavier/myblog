from django.contrib import admin
#
from .models import Favorites
# Register your models here.

class FavoritesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'entry',
    )

admin.site.register(Favorites, FavoritesAdmin)