from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    image = models.ImageField(default='', upload_to='image/')
    caption = models.CharField(max_length=900)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,null=True)
    image = models.ImageField(default='default.jpg', upload_to='project/')
    bio = models.CharField(max_length=200)
    contact = models.IntegerField()
            
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,null=True)
    comment = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="likes")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name="unique_like"),
        ]

