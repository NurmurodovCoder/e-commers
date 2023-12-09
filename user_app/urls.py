from django.urls import path
from .views import RegisterViewAPI


urlpatterns = [
    path('register/', RegisterViewAPI.as_view(), name='register')
]
