from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.SmallIntegerField

class Transaction(models.Model):
    customer = models.ForeignKey
    total = models.PositiveIntegerField
    transaction_datetime = models.DateTimeField("Transaction date")