from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readyonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)