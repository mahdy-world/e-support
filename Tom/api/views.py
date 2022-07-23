from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Tom.models import Tom
from .serializers import TomCreateSerializer

class TomCreateApiVeiw(CreateAPIView):
    queryset = Tom.objects.all()
    serializer_class = TomCreateSerializer