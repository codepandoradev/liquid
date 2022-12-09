from rest_framework import serializers



class NewCoinSerializer(serializers.Serializer):
    coin_short_name = serializers.CharField(max_length=5)
    coin_full_name = serializers.CharField(max_length=255)
    
    
class RemoveCoinSerializer(serializers.Serializer):
    coin_id = serializers.IntegerField()
    

class UserForceUpdateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    nickname = serializers.CharField(max_length=255)
    profile_description = serializers.CharField(max_length=2000)
    user_avatar = serializers.CharField(max_length=1000)
    
    
class RigUpdateSerializer(serializers.Serializer):
    rig_id = serializers.IntegerField()
    details = serializers.ListField()
    energy = serializers.IntegerField()
    wear = serializers.IntegerField()
    # ["nickname","profile_description","user_avatar"]
    