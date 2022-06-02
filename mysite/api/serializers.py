from rest_framework import routers,serializers,viewsets
from crypt.models import User_asset, Coin, Transaction_history

class User_assetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_asset
        fields = ['user_id', 'coins', 'amount', 'average_price']

class Transaction_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_history
        fields = '__all__'

# na razie nie używane
# class CoinSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coin
#         fields = ['coin_id', 'coin_name']
