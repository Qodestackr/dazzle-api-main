from django.contrib import admin
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

models_to_register = [
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
]

# for model in models_to_register:
#     admin.site.register(model)
admin.site.register(models_to_register)