from django.db import models

# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(unique= True, max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username
