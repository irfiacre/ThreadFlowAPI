from django.db import models

class ThreadPosts(models.Model):
    thread_id=models.IntegerField()
    post_id = models.IntegerField()

    def __str__(self) -> str:
        return self.thread_id
