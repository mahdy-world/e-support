from rest_framework.serializers import ModelSerializer
from Tom.models import Tom

class TomCreateSerializer(ModelSerializer):
    class Meta:
        model = Tom
        fields = [
            'merchant',
            'terminalId',
            'station',
            'stationName',
            'officeName'
        ]
