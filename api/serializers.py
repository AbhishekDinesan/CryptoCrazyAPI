#going from python object to JSON

from rest_framework import serializers
from.models import crypto

class CryptoSerializer(serializers.ModelSerializer):
    class Meta: #metadata for model
        model = crypto
        fields = ['date', 'rank', 'price', 'change', 'volume'] #fix the market cap situation