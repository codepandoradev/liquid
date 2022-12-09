from django.urls import path

from .views import ManagementApiView

urlpatterns = [
    path("", ManagementApiView.as_view()),
    path("coin/", ManagementApiView.CoinApiView.as_view()),
    path("user/", ManagementApiView.UserApiView.as_view()),
    path("rigs/", ManagementApiView.RigsApiView.as_view()),
]
