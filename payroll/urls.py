from django.urls import path, re_path, include
from rest_framework import routers
from .views import (PayrollViewSet, PayrollTransactionViewSet,
                    PayrollReportViewSet, TaxViewSet, DeductionViewSet)

router = routers.DefaultRouter()
router.register(r'payroll', PayrollViewSet)
router.register(r'payroll-report', PayrollReportViewSet)
router.register(r'payroll-transactions', PayrollTransactionViewSet)
router.register(r'tax', TaxViewSet)
router.register(r'deductions', DeductionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
