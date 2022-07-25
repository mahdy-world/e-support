from rest_framework.serializers import ModelSerializer
from Tom.models import Tom

class TomCreateSerializer(ModelSerializer):
    class Meta:
        model = Tom
        fields = [
            'merchant',
            'deviceNum',
            'station',
            'stationName',
            'officeEn',
            'officeAr',
            'window',
            'type'
        ]
