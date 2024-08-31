from django.db import models

class Manager(models.Model): 
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"name {self.name}, password {self.password}"
