from django.urls import path, re_path, include
from rest_framework import routers
from .views import EmailViewSet, EmailConfigurationViewSet, MessageViewSet, NoticeBoardViewSet

router = routers.DefaultRouter()

router.register(r'messages', MessageViewSet)
router.register(r'noticeboard', NoticeBoardViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'emailconfigs', EmailConfigurationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
