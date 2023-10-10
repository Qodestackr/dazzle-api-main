from django.db import models
from django.conf import settings
import uuid
from auth_service.models import CustomUser
from common.timestamps import TimeStampedModel
from common.billing import BILLING_POLICY_TEXTS
import os


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


class Billing(models.Model):
    '''
    Django Model: Billing

    This model represents billing information for users in the DazzleHR application.

    Attributes:
        - billing_id (UUIDField): A unique identifier for each billing record.
        - billing_to (ForeignKey): A reference to the user associated with the billing information.
        - billing_plan (CharField): The selected billing plan.
        - auto_renew (BooleanField): Indicates if the billing plan is set to auto-renew.
        - billing_period (DurationField): The billing period duration.
        - payment_status (CharField): The payment status of the billing.
        - payment_method (CharField): The payment method used for billing.

    This model also includes a `billing_policy_text` field to store the billing policy as Markdown text.

    Methods:
        - `get_billing_policy_text()`: Returns the billing policy text for a specific billing instance.

    Usage:
        This model is used to store and manage billing information in the DazzleHR application. 
        It includes a `billing_policy_text` field that is populated with the content of a 
        Markdown file when a new billing record is created(overrides the save method to set the default value for billing_policy_text).

    The `billing_policy_text` field allows you to set a default billing policy text and easily update it by modifying the
    associated Markdown file.

    Please refer to the `save` method for loading the default value of `billing_policy_text` from the `billing_policy.md` file.
    '''

# Your model code here (without repeating the code)

    billing_id = models.UUIDField(primary_key=True, db_index=True)
    billing_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    billing_plan = models.CharField(max_length=255, choices=billing_plan)
    auto_renew = models.BooleanField(default=True)
    billing_period = models.DurationField()
    payment_status = models.CharField(max_length=255, choices=payment_status)
    payment_method = models.CharField(max_length=255, choices=payment_method)
    # montly cost, one-time cost, quarterly cost, yearly cost

    billing_policy_text = models.TextField(default=BILLING_POLICY_TEXTS)


'''    def get_billing_policy_text(self):
        return self.billing_policy_text

    def get_current_monthly_cost(self):
        return 50  # current_monthly_cost

    def update_current_monthly_cost(self):
        return

    def save(self, *args, **kwargs):
        if not self.billing_policy_text:
            # Load content from the Markdown file
            markdown_file_path = os.path.join(
                os.path.dirname(__file__), './billing_policy.md')
            with open(markdown_file_path, 'r') as file:
                self.billing_policy_text = file.read()

        super(Billing, self).save(*args, **kwargs)'''


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
