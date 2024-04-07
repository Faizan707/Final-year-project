from django.db import models

class Assistant(models.Model):
    # Personal Information
    assistantID=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    # Qualification
    qualification = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()

    # Timings
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"