from django.contrib import admin
from cricket.models import Kheladi


@admin.register(Kheladi)
class KheladiAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'age', 'role', ]