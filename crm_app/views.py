from django.shortcuts import render

from django.http import HttpResponse
from .models import Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

def recent_orders(request):
    latest_order_list = Transaction.objects.order_by("transaction_datetime")[:5]
    output = ", ".join([str(o) for o in latest_order_list])
    return HttpResponse(output)