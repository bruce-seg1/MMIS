from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required # Basic protection

# @login_required # Uncomment to protect
def employee_list_view(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'page_title': 'Employee List'
    }
    return render(request, 'hr_payroll/employee_list.html', context)

# @login_required # Uncomment to protect
def employee_detail_view(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    context = {
        'employee': employee,
        'page_title': f"{employee.first_name} {employee.last_name}"
    }
    return render(request, 'hr_payroll/employee_detail.html', context)
