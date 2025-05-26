from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    pass


class Blog(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(null=True, blank=True, default="media/default.png")
    description = models.TextField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"
