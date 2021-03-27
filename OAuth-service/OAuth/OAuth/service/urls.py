from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from OAuth.service.views import UserCreateView, UserListView, is_valid_jwt, Validation
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserListView,)

urlpatterns = [

    path('register/', UserCreateView.as_view()),
    path('user',UserListView),
    path('jwt-validation/',Validation.as_view()),
    #path('auth/',include('rest_framework_social_oauth2.urls')),

]
urlpatterns=urlpatterns+router.urls
