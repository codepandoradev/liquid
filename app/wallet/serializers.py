from rest_framework import serializers


class AskWithdrawSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=200)
    amount = serializers.FloatField()
