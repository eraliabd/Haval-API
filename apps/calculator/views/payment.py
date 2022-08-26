# DRF
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Projects
from calculator.models import Payment
from calculator.serializers import PaymentModelSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.order_by('id')
    serializer_class = PaymentModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['credit']
