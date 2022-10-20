from rest_framework import serializers
from flight_management.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'tx_name',
                  'nm_role',
                  'tx_username',
                  'tx_hash_key')
