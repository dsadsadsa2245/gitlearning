# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from article.views import ArticleViewSet

article_router = routers.DefaultRouter()
article_router.register(r'articles', ArticleViewSet)
