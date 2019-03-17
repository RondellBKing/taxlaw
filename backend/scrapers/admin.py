from django.contrib import admin
from .models import County

class CountyAdmin(admin.ModelAdmin):
    list_display = ('county', 'doc_type')

# Register your models here.

admin.site.register(County, CountyAdmin)
