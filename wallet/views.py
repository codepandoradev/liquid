from django.shortcuts import render

from django.forms import model_to_dict

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AskWithdrawSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


# Create your views here.
class WalletApiView(APIView):
    
    # @extend_schema(
        
    #     request=AskWithdrawSerializer, 
    #     responses={204: None}, 
    #     methods=["POST"])
    # @extend_schema(description='Override a specific method', methods=["POST"])
    # def post(self, request):
    #     return Response({"details":"sample return post"})
        
        
    def get(self,request):
        return Response({"details":"Token does not registred get"})
    
    class AskWithdrawApiView(APIView):
        @extend_schema(
            request=AskWithdrawSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})
        
    
    class PricesApiView(APIView):

        def get(self, request):
            return Response({"details":"sample return get"})
        