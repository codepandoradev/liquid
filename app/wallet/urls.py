from django.urls import path

from .views import WalletApiView
from rest_framework import routers


urlpatterns = [

    path("",WalletApiView.as_view()),
    path("ask_withdraw/",WalletApiView.AskWithdrawApiView.as_view()),
    path("coin_prices/",WalletApiView.PricesApiView.as_view()),
    
]


