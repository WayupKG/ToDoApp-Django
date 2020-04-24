from django.contrib import admin

from .models import Message, User


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'update_date', 'end_date')
    # list_filter = ('status', 'due_back')