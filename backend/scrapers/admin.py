from django.contrib import admin
from .models import County, DocType, DateRange

class ScraperAdmin(admin.ModelAdmin):
    list_display = ('county')

# Register your models here.

admin.site.register(County)
admin.site.register(DocType)
admin.site.register(DateRange)
