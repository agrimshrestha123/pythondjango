from django.db import models

# Create your models here.

# name, gender, profile picture,

class Posts(models.Model):
    POST_CHOICES=[
        (1,'literature'),
        (2,'sports'),
        (3,'technology')
    ]
    author=models.CharField(default="unknown", max_length=100)
    category=models.CharField(choices=POST_CHOICES)
    title=models.CharField(max_length=200)
    image_url=models.URLField(null=True, blank=True)
    status=models.CharField(max_length=20)
    content=models.TextField()
    slug=models.CharField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    


