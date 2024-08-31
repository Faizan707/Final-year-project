from django.db import models

class CustomerAccounts(models.Model):
    name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=50, unique=True)
    customer_fee = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')

    def __str__(self):
        return self.name

class OtherAccounts(models.Model):
    rent_fee = models.DecimalField(max_digits=10, decimal_places=2)
    staff_fee = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
