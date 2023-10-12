from django.urls import path, include
from rest_framework import routers
from .views import AuditViewSet, DatabaseBackupViewSet

router = routers.DefaultRouter()
router.register(r'audits', AuditViewSet)
router.register(r'db-backups', DatabaseBackupViewSet)


urlpatterns = [
    path('', include(router.urls))
]
