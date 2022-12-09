from django.shortcuts import render

from django.forms import model_to_dict

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewRigSerializer,MintRigSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


# Create your views here.
class RigsApiView(APIView):
    
        
    def get(self,request):
        return Response({"details":"Token does not registred get"})
    
    class NewRigApiView(APIView):
        @extend_schema(
            request=NewRigSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})
        
    class MintRigApiView(APIView):
        @extend_schema(
            request=MintRigSerializer, 
            responses={204: None}, 
            methods=["POST"]
        )
        @extend_schema(description='Override a specific method', methods=["POST"])
        def post(self, request):
            return Response({"details":"sample return post"})

        