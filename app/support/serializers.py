from rest_framework import serializers


class NewTicketSerializer(serializers.Serializer):
    theme = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=4000)


class RemoveTicketSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField()
    reason = serializers.CharField(max_length=2000)


class AnswerTicketSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField()
    theme = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=4000)
    close_ticket = serializers.BooleanField(default=False)
