from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Compliance, TaxationPolicy
from .serializers import ComplianceSerializer, TaxationPolicySerializer


class ComplianceViewSet(viewsets.ViewSet):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TaxationPolicyViewSet(viewsets.ViewSet):
    queryset = TaxationPolicy.objects.all()
    serializer_class = TaxationPolicySerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    authentication_classes = [TokenAuthentication]
