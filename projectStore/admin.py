from django.contrib import admin
from .models import Contact, Department, Project, Contact


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('topic', 'type_of_work', 'departments')
    prepopulated_fields = {'slug': ('topic',)}
    search_fields = ('topic', 'type_of_work')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'date' )
    search_fields = ('title', 'name')
    