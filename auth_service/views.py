from rest_framework import viewsets, permissions, authentication
from django.contrib.auth.models import User  # User of CustomUser?
from .models import UserProfile, CustomUser
from .serializers import CustomUserSerializer, UserProfileSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # Require authentication for these views
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # Require authentication for these views
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
