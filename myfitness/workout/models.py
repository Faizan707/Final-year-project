from django.db import models

class Workouts(models.Model):
    customer_id = models.CharField(max_length=50, unique=True)
    day = models.CharField(max_length=20)  
    workout_name = models.CharField(max_length=100)
    exercises = models.TextField()

    def __str__(self):
        return f"Workout for customer ID {self.customer_id} - {self.workout_name} on {self.day}. Exercises: {self.exercises}"
