from django.urls import path, include
from .views import CategoryAPIView, AuthorAPIView, CourseAPIView, BlockAPIView, CommentAPIView, LessonAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', CategoryAPIView)
router.register(r'author', AuthorAPIView)
router.register(r'course', CourseAPIView)
router.register(r'block', BlockAPIView)
router.register(r'comment', CommentAPIView)
router.register(r'lesson', LessonAPIView)


urlpatterns = [
    path('', include(router.urls))
]
