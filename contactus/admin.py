from django.contrib import admin
from .models import HireWriter



@admin.register(HireWriter)
class HireWriterAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number', 'email', 'select_work_type', 'clasification')
    search_fields = ('name','select_work_type', 'clasification')