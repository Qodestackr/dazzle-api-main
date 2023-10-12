from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from common.billing import calculate_prorated_cost
from common.tasks import send_email
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice, Subscription, Billing
from .serializers import BillingSerializer, SubscriptionSerializer, InvoiceSerializer


@api_view(['POST'])
@login_required
def create_invoice(request):
    # You can customize this logic as needed
    # Example logic to create an invoice
    # Total amount initially set to 0
    invoice = Invoice.objects.create(invoice_to=request.user, total_amount=0)
    serializer = BillingSerializer(invoice)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@login_required
def add_billing_item(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    data = request.data  # You should provide the necessary data for the billing item

    # Your logic to add a billing item, calculate total amount, etc.

    # Example calculation of total amount
    invoice.total_amount += data.get('amount', 0)
    invoice.save()

    serializer = BillingSerializer(invoice)
    return Response(serializer.data)


@api_view(['POST'])
@login_required
def subscribe_user(request):
    # Example logic to handle user subscription

    # Get the subscription start date and monthly cost from the request
    subscription_start_date = request.data.get('subscription_start_date')
    monthly_cost = request.data.get('monthly_cost')

    # Calculate the pro-rated cost
    pro_rated_cost = calculate_prorated_cost(
        subscription_start_date, monthly_cost)

    # Create a new subscription record
    subscription = Subscription.objects.create(
        user=request.user,
        subscription_plan=request.data.get('subscription_plan'),
        pro_rated_cost=pro_rated_cost,
    )

    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def send_email_view(request):
    subject = 'Subject of the email'
    message = 'This is the message body.'
    from_email = 'sender@example.com'
    recipient_list = ['recipient@example.com']

    send_email.delay(subject, message, from_email, recipient_list)
    return Response("Email sending task started.")
