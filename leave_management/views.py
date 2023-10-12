from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from .models import (
    LeaveRequest,
    LeaveBalance,
    LeaveAttachment,
    LeaveAccrualRule,
    LeaveApprover,
    LeaveComment,
    LeaveHistory,
    LeaveNotification,
    LeavePolicy,
    LeaveType,
    CustomLeaveField,
    Holiday
)

from .seializers import (
    LeaveRequestSerializer,
    LeaveBalanceSerializer,
    LeaveAttachmentSerializer,
    LeaveAccrualRuleSerializer,
    LeaveApproverSerializer,
    LeaveCommentSerializer,
    LeaveHistorySerializer,
    LeaveNotificationSerializer,
    LeavePolicySerializer,
    LeaveTypeSerializer,
    # CustomLeaveFieldSerializer, #TODO: Exists not
    HolidaySerializer
)


class LeaveRequestViewSet(viewsets.ViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveBalanceViewSet(viewsets.ViewSet):
    queryset = LeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveAttachmentViewSet(viewsets.ViewSet):
    queryset = LeaveAttachment.objects.all()
    serializer_class = LeaveAttachmentSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveAccrualRuleViewSet(viewsets.ViewSet):
    queryset = LeaveAccrualRule.objects.all()
    serializer_class = LeaveAccrualRuleSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveApproverViewSet(viewsets.ViewSet):
    queryset = LeaveApprover.objects.all()
    serializer_class = LeaveApproverSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveCommentViewSet(viewsets.ViewSet):
    queryset = LeaveComment.objects.all()
    serializer_class = LeaveCommentSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveHistoryViewSet(viewsets.ViewSet):
    queryset = LeaveHistory.objects.all()
    serializer_class = LeaveHistorySerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveNotificationViewSet(viewsets.ViewSet):
    queryset = LeaveNotification.objects.all()
    serializer_class = LeaveNotificationSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeavePolicyViewSet(viewsets.ViewSet):
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LeaveTypeViewSet(viewsets.ViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# class CustomLeaveFieldViewSet(viewsets.ViewSet):
#     queryset = CustomLeaveField.objects.all()
#     serializer_class = '....'

#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [TokenAuthentication]


class HolidayViewSet(viewsets.ViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
