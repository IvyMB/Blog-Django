from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
