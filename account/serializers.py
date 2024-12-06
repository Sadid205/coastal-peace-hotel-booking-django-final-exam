from rest_framework import serializers
from .models import Account
class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Account
        fields = '__all__'




class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    def save(self):
        amount = self.validated_data['amount']
        if amount<500:
            raise serializers.ValidationError({"Error":"Please deposit at least 500$."})
        user = self.context['request'].user
        return user,amount
    

