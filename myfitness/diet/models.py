from django.db import models

class Diet(models.Model):
    customer_id = models.CharField(max_length=50)
    break_fast = models.CharField(max_length=50)
    lunch = models.CharField(max_length=50)
    preworkout = models.CharField(max_length=50)
    postworkout = models.CharField(max_length=50)
    dinner = models.CharField(max_length=50)

    def __str__(self):
        return f"Diet plan for Customer ID: {self.customer_id}"
