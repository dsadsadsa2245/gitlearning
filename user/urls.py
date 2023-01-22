from rest_framework import routers

from user.views import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'users', UserViewSet)
