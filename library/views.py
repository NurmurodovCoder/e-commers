from .models import Category, Author, Books
from .serializers import CategorySerializers, AuthorSerializers, BookSerializers

from rest_framework import viewsets


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class AuthorAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BooksAPIView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializers

