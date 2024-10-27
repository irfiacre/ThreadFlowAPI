from django.db import models

# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(unique= True, max_length=50)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default="user", null=True)
    photo_url=models.CharField(max_length=500, null=True)
    biography= models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.username
