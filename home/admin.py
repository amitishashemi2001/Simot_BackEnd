from django.contrib import admin
from .models import SiteInfo, Slider

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'successful_projects')
    # readonly_fields = ('successful_projects',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    search_fields = ('title',)
