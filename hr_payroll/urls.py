from django.urls import path
from . import views

app_name = 'hr_payroll' # Namespace for URLs

urlpatterns = [
    path('employees/', views.employee_list_view, name='employee-list'),
    path('employees/<str:employee_id>/', views.employee_detail_view, name='employee-detail'),
]
