from django.shortcuts import render
from .models import Employee

def create_employee():
    pass


def update_employee():
    pass

def employee_list():
    employees = Employee.objects.all()


def employee_list_department():
    employee_list_department = Employee.objects.filter(department=department) # ? TODO


def employee_active_contract():
    pass


def employee_terminated_contract():
    pass

def employee_pending_contract():
    pass



