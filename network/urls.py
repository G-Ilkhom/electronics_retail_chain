from django.urls import path
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import ContactViewSet, ProductViewSet, NetworkListAPIView, NetworkCreateAPIView, \
    NetworkRetrieveAPIView, NetworkUpdateAPIView, NetworkDestroyAPIView

app_name = NetworkConfig.name

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [path("", NetworkListAPIView.as_view(), name="network_list"),
               path("create/", NetworkCreateAPIView.as_view(), name="network_create"),
               path("<int:pk>/", NetworkRetrieveAPIView.as_view(), name="network_retrieve"),
               path("<int:pk>/update/", NetworkUpdateAPIView.as_view(), name="network_update"),
               path(
                   "<int:pk>/delete/", NetworkDestroyAPIView.as_view(), name="network_delete"
               ),
               ] + contact_router.urls + product_router.urls
