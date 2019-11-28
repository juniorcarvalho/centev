from django.contrib import admin

from crud.core.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telefone']
