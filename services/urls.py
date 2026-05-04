from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceItemListView

urlpatterns = [
    path("list/", ServiceListView.as_view(), name="services_list"),
    path("<int:id>/", ServiceDetailView.as_view(), name="service_detail"),
    path("items/", ServiceItemListView.as_view(), name="service_items"),
]
