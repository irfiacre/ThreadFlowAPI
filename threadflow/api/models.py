from django.db import models
from datetime import datetime

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


class Posts(models.Model):
    message=models.CharField(max_length=1000)
    owner_username = models.CharField(max_length=20)
    created_at = models.CharField(max_length=50, default=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.message


class Threads(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    owner_username = models.CharField(max_length=20)
    photo_url=models.CharField(max_length=500, null=True)
    created_at = models.CharField(max_length=50, default=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.title


class ThreadPosts(models.Model):
    thread_id=models.IntegerField()
    post_id = models.IntegerField()

    def __str__(self) -> str:
        return self.thread_id
