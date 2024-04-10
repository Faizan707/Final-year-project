from django.db import models

class FeeReport(models.Model):
    customer_name=models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
class DueFee(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]

    customer_name = models.CharField(max_length=100)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"

class Salary(models.Model):
    employee_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Profit(models.Model):
     date = models.DateField()
     income = models.DecimalField(max_digits=10, decimal_places=2)
     expenses = models.DecimalField(max_digits=10, decimal_places=2)
     totalprofit=models.DecimalField(max_digits=10, decimal_places=2)

     
class DailyReport(models.Model):
    date = models.DateField()
    total_fees_collected = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    totalprofit=models.DecimalField(max_digits=10, decimal_places=2)

    
class WeeklyReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_fees_collected = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    totalprofit=models.DecimalField(max_digits=10, decimal_places=2)
    
        
    

class YearlyReport(models.Model):
    year = models.IntegerField()
    total_fees_collected = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    totalprofit=models.DecimalField(max_digits=10, decimal_places=2)

class CustomerFitnessReport(models.Model):
    customer_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    bodyfat=models.CharField(max_length=100)
    fitnessLevel=models.CharField(max_length=100)

