from django.contrib import admin
from .models import AboutCompany, CompanyTimeline, Manager

@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'years_experience', 'employees_count', 'completed_projects', 'big_clients')


@admin.register(CompanyTimeline)
class CompanyTimelineAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
