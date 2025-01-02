from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

def detail(request, transaction_id):
    try:
        transaction = Transaction.objects.get(pk=transaction_id)
    except Transaction.DoesNotExist:
        raise Http404("Transaction does not exist")
    return render(request, "crm/detail.html", {"transaction": transaction})

def recent_orders(request):
    latest_order_list = Transaction.objects.order_by("transaction_datetime")[:5]
    context = {
        "latest_order_list": latest_order_list,
    }
    return render(request, "crm/recent_orders.html", context)