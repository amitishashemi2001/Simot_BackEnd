from django.contrib import admin
from .models import CompanyInfo, ContactMessage

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "iran_phone", "uae_phone", "mobile_phone", "email", "uae_address", "iran_address")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
