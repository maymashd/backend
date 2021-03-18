from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from OAuth.service.views import UserCreateView, UserListView

urlpatterns = [

    path('register/', UserCreateView.as_view()),
    path('user/',UserListView),
    path('auth/',include('rest_framework_social_oauth2.urls')),
]
