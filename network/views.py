from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from network.permissions import IsActive
from network.models import Network, Contact, Product
from network.serializers import NetworkSerializer, ContactSerializer, ProductSerializer


class NetworkCreateAPIView(CreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkListAPIView(ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkRetrieveAPIView(RetrieveAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkUpdateAPIView(UpdateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        if "debt_to_supplier" in serializer.validated_data:
            serializer.validated_data.pop("debt_to_supplier")
            raise Exception("Вы не можете обновлять поле 'Задолженность перед поставщиком'")
        super().perform_update(serializer)


class NetworkDestroyAPIView(DestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["country"]
    search_fields = ["country"]
    permission_classes = [IsActive]
