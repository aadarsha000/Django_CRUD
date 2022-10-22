from audioop import add
from django.urls import path
from .views import employee_display, add_employee, update_employee, delete_employee

app_name= "crud"

urlpatterns = [
    path('', employee_display, name="employee_display"),
    path('add/', add_employee, name="add_employee"),
    path('update_employee/<int:id>/', update_employee, name="update_employee" ),
    path('delete_employee/<int:id>/', delete_employee, name="delete_employee" ),
]
