from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number']
    list_filter = ["address"]
    search_fields = ['name']
admin.site.register(Employee, EmployeeAdmin)