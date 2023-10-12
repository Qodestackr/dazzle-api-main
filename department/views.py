from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from .models import Department, Expense
from .seializers import DepartmentSerializer, ExpenseSerializer


class DepartmentViewSet(viewsets.ViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ExpenseViewSet(viewsets.ViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
