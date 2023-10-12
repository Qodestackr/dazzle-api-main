from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    path('auth/', include(router.urls)),  # Include the viewset URLs
]
