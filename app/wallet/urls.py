from django.urls import path

from .views import WalletApiView

urlpatterns = [
    path('', WalletApiView.as_view()),
    path('ask_withdraw/', WalletApiView.AskWithdrawApiView.as_view()),
    path('coin_prices/', WalletApiView.PricesApiView.as_view()),
]
