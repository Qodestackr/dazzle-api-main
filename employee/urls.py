from django.urls import path, include
from rest_framework import routers
from .views import EmployeeSerializer, EmployeeEmergencyContactSerializer

router = routers.DefaultRouter()
router.register(r'employees', EmployeeSerializer)
router.register(r'employee-emergency-contact',
                EmployeeEmergencyContactSerializer)

urlpatterns = [
    path('', include(router.urls))
]
