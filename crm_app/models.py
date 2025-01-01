from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField(default=None)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    total = models.IntegerField()
    transaction_datetime = models.DateTimeField("Transaction date", default=timezone.now)

    def __str__(self):
        return "Transaction amount of $" + str(self.total) + " from customer: " + str(self.customer)