from django.shortcuts import render

from django.forms import model_to_dict

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewCoinSerializer,RemoveCoinSerializer,UserForceUpdateSerializer,RigUpdateSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


# Create your views here.
class ManagementApiView(APIView):
    
    # @extend_schema(
        
    #     request=AskWithdrawSerializer, 
    #     responses={204: None}, 
    #     methods=["POST"])
    # @extend_schema(description='Override a specific method', methods=["POST"])
    # def post(self, request):
    #     return Response({"details":"sample return post"})
        
        
    def get(self,request):
        return Response({"details":"Token does not registred get"})
    
    class CoinApiView(APIView):
        @extend_schema(
            request=NewCoinSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})
        
        
        @extend_schema(
            request=RemoveCoinSerializer, 
            responses={204: None}, 
            methods=["DELETE"]
        )
        @extend_schema(description='Override a specific method', methods=["DELETE"])
        def delete(self, request):
            return Response({"details":"sample return delete"})
        
        
        
    class UserApiView(APIView):
        def get(self,request):
            return Response({"details":"sample return post"})
            
        @extend_schema(
                request=UserForceUpdateSerializer,
                responses={204: None},
                methods=["PATCH"]
        )
        @extend_schema(description='Override a specific method', methods=["PATCH"])
        def patch(self,request):
            return Response({"details":"sample return post"})
        
        
        
    class RigsApiView(APIView):
        def get(self,request):
            return Response({"details":"sample return post"})
            
        @extend_schema(
                request=RigUpdateSerializer,
                responses={204: None},
                methods=["PATCH"]
        )
        @extend_schema(description='Override a specific method', methods=["PATCH"])
        def patch(self,request):
            return Response({"details":"sample return post"})