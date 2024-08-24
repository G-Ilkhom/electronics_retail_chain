from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListAPIView.as_view(), name="users_list"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token-refresh'),
    path("register/", UserCreateAPIView.as_view(), name='register'),
]