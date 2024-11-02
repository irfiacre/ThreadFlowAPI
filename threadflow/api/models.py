from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(unique= True, max_length=50)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default="user", null=True)
    photo_url=models.CharField(max_length=500, null=True)
    biography= models.CharField(max_length=500, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

class Thread(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo_url=models.CharField(max_length=500, null=True, default="https://picsum.photos/700/500")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    is_inappropriate = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    message=models.CharField(max_length=1000)
    owner_username = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.PROTECT, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    is_inappropriate = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.message
