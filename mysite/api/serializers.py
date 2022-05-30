from rest_framework import routers,serializers,viewsets
from crypt.models import User_asset, Coin

class User_assetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_asset
        fields = ['user_id', 'coins', 'ammount', 'average_price']

# na razie nie używane
class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['coin_id', 'coin_name']
