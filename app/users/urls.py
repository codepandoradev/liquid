from django.urls import path

from .views import UserApiView

urlpatterns = [
    path('', UserApiView.as_view()),
    path('verify-email/', UserApiView.VerifyEmailToken.as_view()),
    path('login/', UserApiView.LoginEmail.as_view()),
]
