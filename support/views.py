from django.shortcuts import render

from django.forms import model_to_dict

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewTicketSerializer,RemoveTicketSerializer,AnswerTicketSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


# Create your views here.
class SupportApiView(APIView):
    
    # @extend_schema(
        
    #     request=AskWithdrawSerializer, 
    #     responses={204: None}, 
    #     methods=["POST"])
    # @extend_schema(description='Override a specific method', methods=["POST"])
    # def post(self, request):
    #     return Response({"details":"sample return post"})
        
        
    # def get(self,request):
    #     return Response({"details":"Token does not registred get"})
    
    class NewTicketApiView(APIView):
        @extend_schema(
            request=NewTicketSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})
        
    
    class MyTicketsTicketApiView(APIView):

        def get(self, request):
            return Response({"details":"sample return get"})
    
    class RemoveTicketApiView(APIView):
        @extend_schema(
            request=RemoveTicketSerializer, 
            responses={204: None}, 
            methods=["DELETE"]
        )
        @extend_schema(description='Override a specific method', methods=["DELETE"])
        def delete(self, request):
            return Response({"details":"sample return post"})
        

class SupporterApiView(APIView):
    
    class TicketsApiView(APIView):
        
        def get(self, request):
            return Response({"details":"sample return get"})
    
    class AnswerApiView(APIView):
        
        @extend_schema(
            request=AnswerTicketSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})