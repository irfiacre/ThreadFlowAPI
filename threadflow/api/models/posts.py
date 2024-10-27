from django.db import models
from datetime import datetime

class Posts(models.Model):
    message=models.CharField(max_length=1000)
    owner_username = models.CharField(max_length=20)
    created_at = models.CharField(max_length=50, default=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.message
