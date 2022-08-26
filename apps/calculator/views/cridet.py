# DRF
from rest_framework.viewsets import ModelViewSet

# Projects
from calculator.models import Cridet
from calculator.serializers import CridetModelSerializer


class CreditViewSet(ModelViewSet):
    queryset = Cridet.objects.order_by('id')
    serializer_class = CridetModelSerializer
