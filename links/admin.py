from django.contrib import admin
from .models import URL
# Register your models here.
# admin.site.register(URL)

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'custom_alias', 'expiry', 'clicks')