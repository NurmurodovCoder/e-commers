from django.db import models


class Lang(models.Choices):
    uz = 'UZ'
    ru = 'RU'
    en = 'En'


class Level(models.Choices):
    beginner = 'Beginner'
    hart = 'Hart'
    medium = 'Medium'


class Category(models.Model):
    title = models.CharField(max_length=255)

    book_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField
    img = models.ImageField(upload_to='library/author')

    book_count = models.IntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Books(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    img = models.ImageField(upload_to='library')
    price = models.IntegerField(default=0)
    f_price = models.IntegerField(default=0)
    bio = models.TextField()  # RichText

    page_count = models.IntegerField(default=1)
    published = models.DateField()

    lang = models.CharField(max_length=50, choices=Lang.choices)
    level = models.CharField(max_length=50, choices=Level.choices)

    def __str__(self):
        return self.title
