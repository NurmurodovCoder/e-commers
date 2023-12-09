from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Level(models.TextChoices):
    beginner = 'Beginner',
    hart = 'Hart',
    medium = 'Medium',


class Lang(models.TextChoices):
    uz = "UZ",
    re = "RU",
    en = "en",


class Category(models.Model):
    title = models.CharField(max_length=255)
    course_count = models.IntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='course/author')
    bio = models.TextField()  # RichText boladi

    course_count = models.IntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    img = models.ImageField(upload_to='course')
    lang = models.CharField(max_length=50, choices=Lang.choices)

    block = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    f_price = models.IntegerField(default=0)
    level = models.CharField(max_length=50, choices=Level.choices)

    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def rating(self):
        pass


class Block(models.Model):
    title = models.CharField(max_length=255)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    bio = models.TextField()  # RichTex
    url = models.CharField(max_length=255)

    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='lesson')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')

    def __str__(self):
        return self.title


class Comments(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comment')
    rating = models.IntegerField(default=1)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
