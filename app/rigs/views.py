from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MintRigSerializer, NewRigSerializer


class RigsApiView(APIView):
    def get(self, request):
        return Response({'details': "Token does not registred get"})

    class NewRigApiView(APIView):
        @extend_schema(
            request=NewRigSerializer, responses={204: None}, methods=['POST']
        )
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):
            return Response({'details': "sample return post"})

    class MintRigApiView(APIView):
        @extend_schema(
            request=MintRigSerializer, responses={204: None}, methods=['POST']
        )
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):
            return Response({'details': "sample return post"})
