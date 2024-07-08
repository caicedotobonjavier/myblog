from django.contrib import admin
#
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'full_name',
        'ocupation',
        'genero',
        'date_birth',
        'is_superuser',
        'is_staff',
        'is_active',
    )


admin.site.register(User, UserAdmin)