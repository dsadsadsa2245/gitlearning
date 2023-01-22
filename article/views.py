from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet

from article.models import Article
from article.serializers import ArticleSerializer, ArticleWithoutIdSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ArticleWithoutIdSerializer
        return ArticleSerializer
