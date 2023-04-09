from django.db import models
from django.contrib.auth.models import User


STATUS = {(0, "Draft"), (1, "Publish")}

class Post (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    # ordenação por created_on asc
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
