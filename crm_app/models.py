from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField(default=None)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    total = models.IntegerField()
    transaction_datetime = models.DateTimeField("Transaction date", default=timezone.now)

    def __str__(self):
        return "Transaction amount of $" + str(self.total) + " from customer: " + str(self.customer)