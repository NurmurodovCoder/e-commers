from rest_framework import serializers
from .models import Category, Author, Course, Block, Lesson, Comments


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Category'

        model = Category
        fields = [
            'id',
            'title',
            'course_count',
        ]


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Author'

        model = Author
        fields = [
            'id',
            'full_name',
            'img',
            'bio',
            'course_count',
        ]


class CourseSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    author = AuthorSerializers()

    class Meta:
        ref_name = 'Course'

        model = Course
        fields = [
            'id',
            'title',
            'category',
            'author',
            'img',
            'lang',
            'block',
            'price',
            'f_price',
            'level',
            'create_at'
        ]


class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Block'

        model = Block
        fields = [
            'id',
            'title'
        ]


class LessonSerializers(serializers.ModelSerializer):
    block = BlockSerializers()
    course = CourseSerializers()

    class Meta:
        ref_name = 'Lesson'

        model = Lesson
        fields = [
            'id',
            'title',
            'bio',
            'url',
            'block',
            'course'
        ]


class CommentSerializers(serializers.ModelSerializer):
    course = CourseSerializers()
    # useer = UserSerializers()

    class Meta:
        ref_name = 'Comment'

        model = Comments
        fields = [
            'id',
            'title',
            'user',
            'course',
            'rating',
            'create_at'
        ]
