from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"
    class Meta:
        ordering = ("username",)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="category name")
    description = models.CharField(max_length=255)
    creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Articles(models.Model):
    name = models.CharField(max_length=65)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.category}: ({self.name}"


class Services(models.Model):
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    user = models.ManyToManyField(User, related_name="services")

    def __str__(self):
        return f"{self.name}: ({self.description}{self.category}{self.price})"


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
