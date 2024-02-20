from django.contrib import admin
from .models import WallPaper

class WallPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'slug')
    
admin.site.register(WallPaper, WallPaperAdmin)
