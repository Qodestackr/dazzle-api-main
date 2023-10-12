from django.urls import path, include
from rest_framework import routers
from .views import DepartmentSerializer, ExpenseSerializer

router = routers.DefaultRouter()
router.register(r'departments', DepartmentSerializer)
router.register(r'deparment-expenses',
                ExpenseSerializer)

urlpatterns = [
    path('', include(router.urls))
]
