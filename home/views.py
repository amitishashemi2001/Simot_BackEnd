from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SiteInfo, Slider
from .serializers import SiteInfoSerializer, SliderSerializer


class HomeInfoView(APIView):
    def get(self, request):
        info = SiteInfo.objects.first()
        serializer = SiteInfoSerializer(info)
        return Response(serializer.data)


class SliderListView(APIView):
    def get(self, request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)


class MenuView(APIView):
    def get(self, request):
        menu = [
            {"title": "معرفی خدمات", "slug": "services"},
            {"title": "آموزش", "slug": "education"},
            {"title": "تماس با ما", "slug": "contact"},
            {"title": "درباره ما", "slug": "about"},
            {"title": "گالری تصاویر", "slug": "gallery"},
            {"title": "بخش مدیران", "slug": "managers"},
            {"title": "ورود کاربران", "slug": "login"},
        ]
        return Response(menu)
