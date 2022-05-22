from rest_framework import routers,serializers,viewsets
from crypt.models import User_asset

class User_assetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_asset
        fields = ['user_id', 'coins', 'ammount']
