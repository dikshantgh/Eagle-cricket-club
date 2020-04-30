from django.contrib import admin
from cricket.models import Kheladi, Gang


@admin.register(Kheladi)
class KheladiAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'age', 'role', ]


@admin.register(Gang)
class GangAdmin(admin.ModelAdmin):
    list_display = ['author', 'timestamp', ]