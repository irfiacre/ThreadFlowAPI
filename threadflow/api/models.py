from django.db import models

# Create your models here.

class User(models.Model):
    firstName=models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(unique= True, max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.userName
