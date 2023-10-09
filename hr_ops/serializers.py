from rest_framework import serializers
from .models import Audit, DatabaseBackup


class AuditSerializer(serializers.Serializer):
    class Meta:
        model = Audit
        fields = '__all__'


class DatabaseBackupSerializer(serializers.Serializer):
    class Meta:
        model = DatabaseBackup
        fields = '__all__'
