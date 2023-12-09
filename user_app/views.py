from django.contrib.auth import login
from rest_framework import generics
from .serializers import User, UserSerializer
from rest_framework.response import Response


class RegisterViewAPI(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer

    def create(self, *args, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)
        return Response(serializer.data)

# class LoginViewAPI(generics.CreateAPIView):
#     model = User
#     serializer_class = UserSerializer
    