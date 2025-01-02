from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

def detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, "crm/detail.html", {"transaction": transaction})

def recent_orders(request):
    latest_order_list = Transaction.objects.order_by("transaction_datetime")[:5]
    context = {
        "latest_order_list": latest_order_list,
    }
    return render(request, "crm/recent_orders.html", context)