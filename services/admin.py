from django.contrib import admin
from .models import Service, ServiceItem


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title_fa", "title_en")
    search_fields = ("title_fa", "title_en")


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ("name_fa", "name_en", "service")
    list_filter = ("service",)
    search_fields = ("name_fa", "name_en")
