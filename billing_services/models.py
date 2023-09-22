from django.db import models
import uuid
from auth_service.models import CustomUser

subscription_plan = (
    ('ONE_TIME_USER', 'One-Time User'),
    ('MONTHLY', 'Monthly'),
    ('QUARTERLY', 'Quarterly'),
    ('YEARLY', 'Yearly'),
    ('CUSTOM_AND_UPGRADE', 'Custom and Upgrade'),
)


billing_plan = (
    ('BASIC', 'Basic Plan'),
    ('STANDARD', 'Standard Plan'),
    ('PREMIUM', 'Premium Plan'),
    ('ENTERPRISE', 'Enterprise Plan'),
    ('CUSTOM', 'Custom Plan')
)

payment_method = (
    ('M_PESA', 'Mpesa'),
    ('DAZZLE_WALLET', 'Dazzle Wallet'),
    ('CO-OP_BANK_KENYA', 'Coop bank Kenya'),
    ('EQUITY_BANK_KENYA', 'Equity Bank Kenya'),
    ('PAYPAL', 'Paypal'),
    ('VISA_CARD', 'Visa Card'),
    ('MASTER_CARD', 'Master Card'),
    ('FLUTTERWAVE', 'Flutterwave')
)

payment_status = (
    ('PENDING', 'Pending'),
    ('SUCCESS', 'Success'),
    ('FAILED', 'Failed'),
)


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    '''
    cls is a conventional name for the first parameter of a class method in Python. 
    It stands for "class" and is a reference to the class itself, not an instance of the class. 
    It allows to access and manipulate class-level attributes and behaviors.
    cls._meta refers to the options or metadata of the class.
    SIMPLY PUT: We do this to operate on the class itself and not an instance of a class (unlike `self`)
    '''

    @classmethod
    def set_ordering(cls, ordering):
        cls._meta.ordering = ordering


class Billing(TimestampedModel):
    billing_id = models.UUIDField(
        primary_key=True, default=uuid.uuid5, db_index=True)
    billing_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    billing_plan = models.CharField(max_length=255, choices=billing_plan)
    auto_renew = models.BooleanField(default=True)
    billing_period = models.DurationField()

    payment_status = models.CharField(max_length=255, choices=payment_status)

    payment_method = models.CharField(max_length=255, choices=payment_method)


class Subscription(TimestampedModel):
    subscription_id = models.UUIDField(
        primary_key=True, default=uuid.uuid5, db_index=True)
    subscription_plan = models.CharField(
        max_length=255, choices=subscription_plan)

    TimestampedModel.set_ordering('created_at')


class Invoice(TimestampedModel):
    invoice_id = models.UUIDField(
        primary_key=True, default=uuid.uuid5, unique=True, db_index=True,)
    invoice_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)

    TimestampedModel.set_ordering('created_at')
