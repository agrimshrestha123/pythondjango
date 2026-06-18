from django.db import models

# Create your models here.

# name, gender, profile picture,

class Posts(models.Model):
    POST_CHOICES=[
        ('l','literature'),
        ('s','sports'),
        ('t','technology')
    ]
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    author=models.CharField(default="unknown", max_length=100)
    category=models.CharField(choices=POST_CHOICES)
    title=models.CharField(max_length=200)
    image_url=models.URLField(null=True, blank=True)
    status=models.CharField(max_length=20)
    content=models.TextField()
    slug=models.CharField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author

    def create_slug(self):
        slug=self.slug

