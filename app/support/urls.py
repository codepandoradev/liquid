from django.urls import path

from .views import SupportApiView,SupporterApiView
from rest_framework import routers


urlpatterns = [

    path("me/new_ticket",SupportApiView.NewTicketApiView.as_view()),
    path("me/revoke_ticket",SupportApiView.RemoveTicketApiView.as_view()),
    path("supporter/ask_tiket",SupporterApiView.AnswerApiView.as_view()),
    path("supporter/avaliable_tickets",SupporterApiView.TicketsApiView.as_view())
    
]


