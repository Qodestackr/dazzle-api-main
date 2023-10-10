from django.db import models
from common.timestamps import TimeStampedModel
from employee.models import Employee


class Payroll(TimeStampedModel):
    """
    A payroll record for an employee.

    Fields:
        employee: The employee associated with this payroll record.
        payroll_id: A unique identifier for this payroll record.
        main_salary: The employee's base salary.
        total_compensation_amount: The total amount of compensation paid to the employee, including base salary, bonuses, and allowances.
        allowance_amount: The total amount of allowances paid to the employee.
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll_id = models.CharField(max_length=255, unique=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)
    allowance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_rate = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)


class Tax(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_type = models.CharField(max_length=255, choices=[('INCOME_TAX', 'Income Tax'), ('PAYE', 'Pay As You Earn'), (
        'NHIF', 'National Hospital Insurance Fund'), ('NSSF', 'National Social Security Fund'), ('HDMF', 'Home Development Mutual Fund')])
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Taxes'


class Deduction(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deduction_type = models.CharField(max_length=255)
    deduction_amount = models.DecimalField(max_digits=10, decimal_places=2)


class PayrollTransaction(TimeStampedModel):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()


class PayrollReport(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll_period = models.CharField(max_length=255)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)
    allowance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_rate = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deduction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
