from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'date_added', 'owner')
    search_fields = ('title', 'description')
    list_filter = ('date_added', 'owner')


