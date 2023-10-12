from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Audit, DatabaseBackup
from .serializers import AuditSerializer, DatabaseBackupSerializer


class AuditViewSet(viewsets.ViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DatabaseBackupViewSet(viewsets.ViewSet):
    queryset = DatabaseBackup.objects.all()
    serializer_class = DatabaseBackupSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
