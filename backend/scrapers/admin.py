from django.contrib import admin
from .models import County, Lien, LienItem

class CountyAdmin(admin.ModelAdmin):
    list_display = ('county')

# Register your models here.

admin.site.register(County)
admin.site.register(Lien)
# admin.site.register(LienItem)
