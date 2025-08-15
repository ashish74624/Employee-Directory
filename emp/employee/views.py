from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def employee_page(request, slug):
    employee = Employee.objects.get(email=slug)
    return render(request, 'employees/employee_page.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_dir:list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, slug):
    employee = Employee.objects.get(email=slug)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_dir:list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_update_form.html', {'form': form})

def employee_delete(request, slug):
    employee = Employee.objects.get(email=slug)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_dir:list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
    
    