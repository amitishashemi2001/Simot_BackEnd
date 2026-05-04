from django.urls import path
from .views import CompanyInfoView, ContactMessageCreateView

urlpatterns = [
    path("info/", CompanyInfoView.as_view(), name="company_info"),
    path("send/", ContactMessageCreateView.as_view(), name="contact_send"),
]
