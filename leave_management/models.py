from django.db import models
from employee.models import TimestampedModel, Employee, EmployeeEmergencyContact


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[(
        'pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])


class LeaveType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"


class LeaveAccrualRule(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    accrual_rate = models.DecimalField(max_digits=5, decimal_places=2)
    accrual_frequency = models.CharField(
        max_length=20, choices=[('monthly', 'Monthly'), ('annually', 'Annually')])

    def __str__(self):
        return f"{self.leave_type} - {self.accrual_rate} per {self.accrual_frequency}"


class LeavePolicy(models.Model):
    name = models.CharField(max_length=100)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    applicable_employees = models.ManyToManyField(Employee)
    maximum_leave_balance = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other policy-specific fields

    def __str__(self):
        return self.name


class Holiday(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.description}"


class LeaveApprover(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    approver = models.ForeignKey(
        Employee, related_name='leave_approvers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.approver} approves leave for {self.employee}"


class LeaveHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[(
        'pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"{self.employee} - {self.leave_type} - {self.start_date} to {self.end_date}"


class LeaveNotification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.employee}"


class LeaveAttachment(models.Model):
    leave_request = models.ForeignKey(LeaveHistory, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='leave_attachments/')

    def __str__(self):
        return f"Attachment for {self.leave_request}"


class LeaveComment(models.Model):
    leave_request = models.ForeignKey(LeaveHistory, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment for {self.leave_request}"


class CustomLeaveField(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # Add other field attributes as needed

    def __str__(self):
        return self.name
