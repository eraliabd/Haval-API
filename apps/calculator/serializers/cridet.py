from rest_framework import serializers

# Project
from calculator.models import Cridet


class CridetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cridet
        fields = "__all__"
