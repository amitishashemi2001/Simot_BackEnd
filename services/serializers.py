from rest_framework import serializers
from .models import Service, ServiceItem


class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    items = ServiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
