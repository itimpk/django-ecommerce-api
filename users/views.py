# users/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny # Allow anyone to register

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,) # Allow unauthenticated users to register

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # You can customize the response here, e.g., only return username/email
        response_data = {
            "username": serializer.data["username"],
            "email": serializer.data["email"],
            "message": "User registered successfully."
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)