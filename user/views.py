import random
from django.core.mail import send_mail

from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from article.models import Article
from project.settings import EMAIL_HOST_USER
from user.models import User
from user.serializers import UserSerializer


# Create your views here.
class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        pass_code = random.randint(1000, 9999)
        pass_code = str(pass_code)

        user = serializer.save(is_active=False, code=pass_code)
        response = send_mail(
            'verification',
            pass_code,
            EMAIL_HOST_USER,
            [user.email],
        )

