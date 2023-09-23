from django.shortcuts import render, HttpResponse
from .models import CustomUser

def CreateUser():
    model = CustomUser
    fields = [
        'email',
        'company_name',
        'company_address',
        'industry',
        'employee_count',
        'contact_person_name',
        'contact_email',
        'phone_number',
        'subdomain',
    ]


def UpdateUser():
    models = CustomUser

    fields = [

    ]


def DeleteUser():
    model = CustomUser


def UserList(request):
    users = CustomUser.objects.all()

    return HttpResponse(users)


# https://reintech.io/blog/creating-a-custom-user-management-system-in-django