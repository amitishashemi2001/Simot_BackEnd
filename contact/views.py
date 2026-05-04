from rest_framework import generics
from .models import CompanyInfo, ContactMessage
from .serializers import CompanyInfoSerializer, ContactMessageSerializer

# نمایش اطلاعات شرکت
class CompanyInfoView(generics.RetrieveAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

    def get_object(self):
        return self.queryset.first()  # فقط اولین رکورد را برمی‌گرداند

# ثبت پیام تماس
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
