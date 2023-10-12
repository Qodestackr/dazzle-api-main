from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Payroll, PayrollReport, PayrollTransaction, Deduction, Tax
from .serializers import (
    PayrollSerializer,
    PayrollReportSerializer,
    PayrollTransactionSerializer,
    DeductionSerializer,
    TaxSerializer)


class PayrollViewSet(viewsets.ViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

    authentication_classes = [permissions.IsAuthenticated]
    permission_classes = [TokenAuthentication]


class PayrollReportViewSet(viewsets.ViewSet):
    queryset = PayrollReport.objects.all()
    serializer_class = PayrollReportSerializer

    permission_classes = [permissions.IsAuthenticated,
                          permissions.IsAdminUser, ]
    authentication_classes = [TokenAuthentication]


class PayrollTransactionViewSet(viewsets.ViewSet):
    queryset = PayrollTransaction.objects.all()
    serializer_class = PayrollTransactionSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DeductionViewSet(viewsets.ViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TaxViewSet(viewsets.ViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
