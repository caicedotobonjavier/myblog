from django.contrib import admin
#
from .models import Home, Suscribers, Contact
# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'about_title',
        'about_text',
        'contat_email',
        'phone',
    )


admin.site.register(Home, HomeAdmin)


class SuscribersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
    )


admin.site.register(Suscribers, SuscribersAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'messagge',
    )

admin.site.register(Contact, ContactAdmin)