from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Transaction, Customer
import datetime

def create_customer():
    return Customer(name="tyler", phone_number = 123, email = "ty@g.com")

def create_transaction(customer, days):
    """
    Create a transaction with the given `transaction_text` and published the
    given number of `days` offset to now (negative for orders published
    in the past, positive for orders that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Transaction.objects.create(transaction_datetime=time, total = 0, customer=customer)


class RecentOrdersViewTests(TestCase):
    def test_no_orders(self):
        """
        If no orders exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("crm_app:recent orders"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No transactions are available.")
        self.assertQuerySetEqual(response.context["latest_order_list"], [])


    def test_past_order(self):
        """
        orders with a pub_date in the past are displayed on the
        recent_orders_generic page.
        """
        customer = create_customer()
        customer.save()
        order = create_transaction(customer, days=-30)
        response = self.client.get(reverse("crm_app:recent orders"))
        self.assertQuerySetEqual(
            response.context["latest_order_list"],
            [order],
        )

    def test_future_order(self):
        #if order is in future, it's not displayed
        customer = create_customer()
        customer.save()
        create_transaction(customer, days=30)
        response = self.client.get(reverse("crm_app:recent orders"))
        self.assertContains(response, "No transactions are available.")
        self.assertQuerySetEqual(response.context["latest_order_list"], [])

    def test_future_order_and_past_order(self):
        """
        Even if both past and future orders exist, only past orders
        are displayed.
        """
        customer = create_customer()
        customer.save()
        order = create_transaction(customer, days=-30)
        order2 = create_transaction(customer, days=30)
        response = self.client.get(reverse("crm_app:recent orders"))
        self.assertQuerySetEqual(
            response.context["latest_order_list"],
            [order],
        )

    def test_two_past_orders(self):
        """
        The orders recent_orders_generic page may display multiple orders.
        """
        customer = create_customer()
        customer.save()
        order1 = create_transaction(customer,days=-30)
        order2 = create_transaction(customer,days=-5)
        response = self.client.get(reverse("crm_app:recent orders"))
        self.assertQuerySetEqual(
            response.context["latest_order_list"],
            [order1, order2],
        )