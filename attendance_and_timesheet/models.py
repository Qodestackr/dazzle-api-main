from django.db import models
from employee.models import Employee
from common.timestamps import TimeStampedModel


class AttendanceRecord(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"


class TimesheetRecord(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    project_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.date}"


class Holiday(TimeStampedModel):
    '''
    TODO: Auto load country specific Holidays
    '''
    date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.description}"


'''
Attendance: In some cases, organizations track holidays in their attendance records to account 
for non-working days when employees are not expected to be present at work. This helps in calculating 
attendance and working hours more accurately.

Leave Management: Holidays can also be crucial in leave management. Employees might request time 
off during holidays, and organizations need to account for holidays when calculating leave balances 
and processing leave requests.
'''
