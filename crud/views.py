from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_display(request):
    employee = Employee.objects.all()
    return render(request, 'index.html', {'employee':employee})

def add_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:employee_display')
        else:
            form = EmployeeForm()
    return render(request, 'add.html', {'form':form})

def update_employee(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    if form.is_valid():
            form.save()
            return redirect('crud:employee_display')
    return render(request, 'update.html', {'form':form})

def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('crud:employee_display')

