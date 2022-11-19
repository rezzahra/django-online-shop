from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
