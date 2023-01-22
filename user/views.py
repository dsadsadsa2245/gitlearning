from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet

from article.models import Article
from user.models import User
from user.serializers import UserSerializer


# Create your views here.
class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
