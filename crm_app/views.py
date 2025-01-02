from django.shortcuts import render, get_object_or_404

from django.db.models import F
from django.http import HttpResponse
from django.views import generic
from .models import Transaction, Customer


def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")



class DetailView(generic.DetailView):
    model = Transaction
    template_name = "crm/detail.html"

def recent_orders(request):
    latest_order_list = Transaction.objects.order_by("transaction_datetime")[:5]
    context = {
        "latest_order_list": latest_order_list,
    }
    return render(request, "crm/recent_orders.html", context)