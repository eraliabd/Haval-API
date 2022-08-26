# DRF
from rest_framework import serializers

# Projects
from calculator.serializers.calculator_handbook import CarCridetCalcModelSerializer, CarLeasingCalcModelSerializer


class CalculateSerializer(serializers.Serializer):
    credit = CarCridetCalcModelSerializer(many=True, read_only=True)
    leasing = CarLeasingCalcModelSerializer(many=True, read_only=True)