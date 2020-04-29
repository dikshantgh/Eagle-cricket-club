from django.contrib import admin

# Register your models here.
from chat.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'timestamp', ]