from rest_framework import serializers
from .models import (
    LeaveRequest,
    LeaveType,
    LeaveBalance,
    LeaveAccrualRule,
    LeavePolicy,
    Holiday,
    LeaveApprover,
    LeaveHistory,
    LeaveNotification,
    LeaveAttachment,
    LeaveComment,
    # CustomLeaveField
)


class LeaveRequestSerializer(serializers.Serializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'


class LeaveTypeSerializer(serializers.Serializer):
    class Meta:
        model = LeaveType
        fields = '__all__'


class LeaveBalanceSerializer(serializers.Serializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'


# r-------
class LeaveAccrualRuleSerializer(serializers.Serializer):
    class Meta:
        model = LeaveAccrualRule
        fields = '__all__'


class LeavePolicySerializer(serializers.Serializer):
    class Meta:
        model = LeavePolicy
        fields = '__all__'


class HolidaySerializer(serializers.Serializer):
    class Meta:
        model = Holiday
        fields = '__all__'


class LeaveApproverSerializer(serializers.Serializer):
    class Meta:
        model = LeaveApprover
        fields = '__all__'


class LeaveHistorySerializer(serializers.Serializer):
    class Meta:
        model = LeaveHistory
        fields = '__all__'


class LeaveNotificationSerializer(serializers.Serializer):
    class Meta:
        model = LeaveNotification
        fields = '__all__'


class LeaveAttachmentSerializer(serializers.Serializer):
    class Meta:
        model = LeaveAttachment
        fields = '__all__'


class LeaveCommentSerializer(serializers.Serializer):
    class Meta:
        model = LeaveComment
        fields = '__all__'
