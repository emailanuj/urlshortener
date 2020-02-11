from django.contrib import admin
from .models import short_urls
# Register your models here.
class URLAdmin(admin.ModelAdmin):
    list_display=['long_url','short_url','timestamp']
admin.site.register(short_urls,URLAdmin)
