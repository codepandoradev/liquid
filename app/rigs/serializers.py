from rest_framework import serializers



class NewRigSerializer(serializers.Serializer):
    rig_details = serializers.ListField()
    
    
class MintRigSerializer(serializers.Serializer):
    rig_id = serializers.IntegerField()

    