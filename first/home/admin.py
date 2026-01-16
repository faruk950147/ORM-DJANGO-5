from django.contrib import admin
from home.models import University, Department

# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'established_year', 'is_public', 'ranking', 'website', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('is_public', 'established_year')
    ordering = ('-established_year',)
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'head_of_department', 'established_year')
    search_fields = ('name', 'university__name')
    list_filter = ('established_year',)
    ordering = ('name',)