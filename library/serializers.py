from rest_framework import serializers
from .models import Category, Author, Books


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'book_count'
        ]


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'full_name',
            'bio',
            'img',
            'book_count',
            'create_at'
        ]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'title',
            'category',
            'author',
            'img',
            'price',
            'f_price',
            'bio',
            'page_count',
            'published',
            'lang',
            'level'
        ]

