# DRF
from rest_framework import serializers

# Projects
from automobile.models import Car, PositionCategory
from calculator.models import Cridet
from calculator.serializers import PaymentModelSerializer


class CridetsCalcSerializer(serializers.ModelSerializer):
    payment = PaymentModelSerializer(source='payments', many=True, read_only=True)

    class Meta:
        model = Cridet
        fields = [
            'month',
            'payment',
        ]


class LeasingCalcSerializer(serializers.ModelSerializer):
    payment = PaymentModelSerializer(source='payments', many=True, read_only=True)

    class Meta:
        model = Cridet
        fields = [
            'month',
            'payment',
        ]


class PositionCridetCalcModelSerializer(serializers.ModelSerializer):
    credit = CridetsCalcSerializer(source='cridets', many=True, read_only=True)

    class Meta:
        model = PositionCategory
        fields = [
            'id',
            'name',
            'credit',
        ]

class PositionLeasingCalcModelSerializer(serializers.ModelSerializer):
    leasing = LeasingCalcSerializer(source='cridets', many=True, read_only=True)

    class Meta:
        model = PositionCategory
        fields = [
            'id',
            'name',
            'leasing',
        ]

class CarCridetCalcModelSerializer(serializers.ModelSerializer):
    models = PositionCridetCalcModelSerializer(source='positioncategory_set', many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'models',
        ]


class CarLeasingCalcModelSerializer(serializers.ModelSerializer):
    models = PositionLeasingCalcModelSerializer(source='positioncategory_set', many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'models',
        ]