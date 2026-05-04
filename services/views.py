from rest_framework import generics
from .models import Service, ServiceItem
from .serializers import ServiceSerializer, ServiceItemSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "id"


class ServiceItemListView(generics.ListAPIView):
    queryset = ServiceItem.objects.all()
    serializer_class = ServiceItemSerializer
