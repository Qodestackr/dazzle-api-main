from django.db import models
import uuid
from auth_service.models import CustomUser
from common.timestamps import TimeStampedModel

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


class Billing(TimeStampedModel):
    billing_id = models.UUIDField(
        primary_key=True, db_index=True)  #
    billing_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    billing_plan = models.CharField(max_length=255, choices=billing_plan)
    auto_renew = models.BooleanField(default=True)
    billing_period = models.DurationField()

    payment_status = models.CharField(max_length=255, choices=payment_status)

    payment_method = models.CharField(max_length=255, choices=payment_method)


class Subscription(TimeStampedModel):
    subscription_id = models.UUIDField(
        primary_key=True, db_index=True)  # default=uuid.uuid5(namespace='', name=''),
    subscription_plan = models.CharField(
        max_length=255, choices=subscription_plan)

    TimeStampedModel.set_ordering('created_at')


class Invoice(TimeStampedModel):
    invoice_id = models.UUIDField(
        primary_key=True, unique=True, db_index=True,)  # default=uuid.uuid5(namespace='', name=''),

    invoice_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)

    TimeStampedModel.set_ordering('created_at')
