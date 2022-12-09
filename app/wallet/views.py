from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AskWithdrawSerializer


class WalletApiView(APIView):
    def get(self, request):
        return Response({'details': "Token does not registred get"})

    class AskWithdrawApiView(APIView):
        @extend_schema(
            request=AskWithdrawSerializer, responses={204: None}, methods=['POST']
        )
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):
            return Response({'details': "sample return post"})

    class PricesApiView(APIView):
        def get(self, request):
            return Response({'details': "sample return get"})
