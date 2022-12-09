from django.urls import path
from .views import create_user
from .views import UserApiView
from rest_framework import routers


urlpatterns = [
    # path("",UserApiView.as_view()),
    # path("create_user/phone_number/",UserApiView.as_view()),
    path("",UserApiView.as_view()),
    path("verify-email/",UserApiView.VerifyEmailToken.as_view()),
    path("login/",UserApiView.LoginEmail.as_view()),
    
]


