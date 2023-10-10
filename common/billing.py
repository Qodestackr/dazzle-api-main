from datetime import datetime, timedelta


def calculate_prorated_cost(subscription_start_date, monthly_cost):
    # Define the end of the billing cycle (e.g., end of the month)
    end_of_billing_cycle = subscription_start_date.replace(day=30)

    # Calculate the number of days remaining in the billing cycle
    days_remaining = (end_of_billing_cycle - subscription_start_date).days + 1

    # Calculate the daily rate
    daily_rate = monthly_cost / 30  # Assuming 30 days in a month

    # Calculate the pro-rated cost
    pro_rated_cost = daily_rate * days_remaining

    return pro_rated_cost


# Example usage
subscription_start_date = datetime(2023, 9, 17)
monthly_cost = 50  # Example monthly cost
prorated_cost = calculate_prorated_cost(subscription_start_date, monthly_cost)
print(f"Pro-rated cost: ${prorated_cost:.2f}")


'''
Calculating a pro-rata or partial month subscription when a user's subscription starts on a day other than the 1st or 2nd of the month is a common challenge in billing systems. To handle this, you typically need to determine the number of days remaining in the current billing cycle and charge the user accordingly. Here's a general approach to address this situation:

Define Billing Cycle: First, establish a billing cycle for your subscriptions. This cycle could be based on a specific day of the month, like the 1st or 2nd, but it doesn't have to be. For example, you could use the day the user subscribes as the start of their billing cycle.

Trial Period: If you have a trial period (e.g., 14 days), consider this as part of the billing cycle.

Calculate Days Remaining: Determine the number of days remaining in the current billing cycle. This can be calculated by finding the difference between the subscription start date and the end of the billing cycle.

Prorate Subscription Cost: Calculate the pro-rated cost for the remaining days of the current billing cycle. To do this, divide the total monthly cost by the number of days in a month (you can assume 30 or 31 days for simplicity) to get a daily rate. Then, multiply this daily rate by the number of days remaining in the billing cycle.
'''


BILLING_POLICY_TEXTS = """
## DazzleHR Billing Policy
DazzleHR is a Software-as-a-Service (SaaS) HR system designed to streamline your organization's human resources management. This Billing Policy outlines the terms and conditions regarding subscription, billing, and payment for DazzleHR's services. By using DazzleHR, you agree to abide by this Billing Policy.

### Subscription and Billing
<!-- TODO: Do not accept if Scoll is not to the end -->
1. Subscription Terms
DazzleHR offers various subscription plans with different features and pricing. Subscribers may choose a plan that suits their organization's needs.

Subscriptions are billed on a recurring basis (e.g., one-time purchaase, monthly, quarterly, or annually), depending on the chosen plan.

Your subscription will automatically renew at the end of each billing period unless canceled. End of a free plan does not trigger auto bill, we let you activate that, an email will be triggered at the end of 14 days free trial.

2. Payment
Subscribers are required to provide valid payment information and agree to pay the subscription fees associated with their chosen plan.

Payment methods accepted by DazzleHR include credit/debit cards or other forms as specified on our website.

3. Billing Cycle
The billing cycle depends on the selected subscription plan and starts on the date of initial subscription activation.

Subscribers will be billed in advance for their chosen billing period.

4. Cancellation
Subscribers can cancel their subscription at any time by visiting the Billing section on the DazzleHR platform.

Once canceled, the subscription will remain active until the end of the current billing period.

DazzleHR does not provide refunds for any amounts already charged for subscription cancellation.

5. Subscription Renewal
DazzleHR automatically renews subscriptions at the end of each billing period unless canceled by the subscriber.

Renewals are based on the originally chosen plan and payment method, unless updated by the subscriber.

Access and Termination
DazzleHR reserves the right to deny access to any part of the service or terminate an organization's account, with or without notice, if it is found that the subscriber has violated the terms of this Billing Policy or DazzleHR's Terms of Service.

Termination may occur without providing a refund or partial refund.

Contact Information
If you have any questions or concerns regarding this Billing Policy, please contact our billing team at billing@dazzlehr.com.

Please make sure to adapt this policy to your specific terms and conditions, and ensure that it complies with any legal or regulatory requirements in your jurisdiction. Additionally, you may want to include information on pricing, available subscription plans, and payment methods on your website or within the policy itself.
"""
