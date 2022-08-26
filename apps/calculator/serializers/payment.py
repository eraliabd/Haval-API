from rest_framework import serializers

# Project
from calculator.models import Payment


class PaymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'sum', 'percent', 'total', 'remain']  # "__all__"
