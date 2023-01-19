from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from article.models import Article
from article.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
