from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["login","password","user_email","phone_number","client_name"]
        


class AskWithdrawSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=200)
    amount = serializers.FloatField()
    
    
        

        
