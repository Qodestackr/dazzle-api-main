from django.urls import path, include
from rest_framework import routers

from .views import (LeaveRequestViewSet,
                    LeaveBalanceViewSet, LeaveAttachmentViewSet,
                    LeaveAccrualRuleViewSet, LeaveApproverViewSet,
                    LeaveCommentViewSet, LeaveHistoryViewSet,
                    LeaveNotificationViewSet, LeavePolicyViewSet,
                    LeaveTypeViewSet, CustomLeaveFieldViewSet, HolidayViewSet)


router = routers.DefaultRouter()

router.register(r'leave-request', LeaveRequestViewSet)
router.register(r'leave-balances', LeaveBalanceViewSet)
router.register(r'leave-attachments', LeaveAttachmentViewSet)
router.register(r'leave-accrual', LeaveAccrualRuleViewSet)
router.register(r'leave-approver', LeaveApproverViewSet)
router.register(r'leave-comments', LeaveCommentViewSet)
router.register(r'leave-history', LeaveHistoryViewSet)
router.register(r'leave-notifications', LeaveNotificationViewSet)
router.register(r'leave-policies', LeavePolicyViewSet)
router.register(r'leave-type', LeaveTypeViewSet)
# router.register(r'leave-custom-field', CustomLeaveFieldViewSet)
router.register(r'leave-holidays', HolidayViewSet)


urlpatterns = [
    path('', include(router.urls))
]
