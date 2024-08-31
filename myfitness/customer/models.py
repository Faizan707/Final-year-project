from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height_inches = models.PositiveIntegerField()
    height_feet = models.PositiveIntegerField()
    fitness_goal = models.TextField()
    instructor_id =models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}-{self.id}"
