from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    AnswerTicketSerializer,
    NewTicketSerializer,
    RemoveTicketSerializer,
)


class SupportApiView(APIView):
    class NewTicketApiView(APIView):
        @extend_schema(
            request=NewTicketSerializer, responses={204: None}, methods=['POST']
        )
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):
            return Response({'details': "sample return post"})

    class MyTicketsTicketApiView(APIView):
        def get(self, request):
            return Response({'details': "sample return get"})

    class RemoveTicketApiView(APIView):
        @extend_schema(
            request=RemoveTicketSerializer, responses={204: None}, methods=['DELETE']
        )
        @extend_schema(description="Override a specific method", methods=['DELETE'])
        def delete(self, request):
            return Response({'details': "sample return post"})


class SupporterApiView(APIView):
    class TicketsApiView(APIView):
        def get(self, request):
            return Response({'details': "sample return get"})

    class AnswerApiView(APIView):
        @extend_schema(
            request=AnswerTicketSerializer, responses={204: None}, methods=['POST']
        )
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):
            return Response({'details': "sample return post"})
