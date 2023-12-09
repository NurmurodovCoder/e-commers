from .models import Category, Author, Course, Block, Comments, Lesson
from rest_framework import viewsets

from .serializers import CategorySerializers, AuthorSerializers, CourseSerializers, BlockSerializers, \
    CommentSerializers, LessonSerializers


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class AuthorAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class CourseAPIView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class BlockAPIView(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializers


class LessonAPIView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializers
