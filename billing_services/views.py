from email import message
from django.shortcuts import render, redirect
import uuid

from .models import Invoice, Subscription, Billing



# Invoice: https://python.plainenglish.io/build-a-complete-invoicing-web-application-with-django-8e6c56745935
@login_required()
def create_invoice(request):
    # Blank invoice

    number = 'INV' + str(uuid.uuid5()).split('-')[1]
    new_invoice = Invoice.objects.create(number=number)

    new_invoice.save

    inv = Invoice.objects.get(number=number)

    return redirect('create-build-invoice', slug=inv.slug)



@login_required
def create_build_invoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        message.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Billing.objects.filter(invoice=invoice)


    context = {}
    context['invoice'] = invoice
    context['products'] = products

    # if request.method == 'GET':
    #     prod_form  = ProductForm()
    #     inv_form = InvoiceForm(instance=invoice)
    #     client_form = ClientSelectForm(initial_client=invoice.client)
    #     context['prod_form'] = prod_form
    #     context['inv_form'] = inv_form
    #     context['client_form'] = client_form
    #     return render(request, 'invoice/create-invoice.html', context)

    # if request.method == 'POST':
    #     prod_form  = ProductForm(request.POST)
    #     inv_form = InvoiceForm(request.POST, instance=invoice)
    #     client_form = ClientSelectForm(request.POST, initial_client=invoice.client, instance=invoice)

    #     if prod_form.is_valid():
    #         obj = prod_form.save(commit=False)
    #         obj.invoice = invoice
    #         obj.save()

    #         messages.success(request, "Invoice product added succesfully")
    #         return redirect('create-build-invoice', slug=slug)
    #     elif inv_form.is_valid and 'paymentTerms' in request.POST:
    #         inv_form.save()

    #         messages.success(request, "Invoice updated succesfully")
    #         return redirect('create-build-invoice', slug=slug)
    #     elif client_form.is_valid() and 'client' in request.POST:

    #         client_form.save()
    #         messages.success(request, "Client added to invoice succesfully")
    #         return redirect('create-build-invoice', slug=slug)
    #     else:
    #         context['prod_form'] = prod_form
    #         context['inv_form'] = inv_form
    #         context['client_form'] = client_form
    #         messages.error(request,"Problem processing your request")
    #         return render(request, 'invoice/create-invoice.html', context)


    return render(request, 'invoice/create-invoice.html', context)