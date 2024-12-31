from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField(default=1)
    email = models.EmailField(default=None)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    total = models.IntegerField(default=1)
    transaction_datetime = models.DateTimeField("Transaction date")

    def __str__(self):
        return "Transaction amount of $" + str(self.total) + " from customer: " + self.customer