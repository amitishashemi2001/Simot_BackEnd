from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutCompany, CompanyTimeline, Manager
from .serializers import AboutCompanySerializer, CompanyTimelineSerializer, ManagerSerializer

class AboutPageView(APIView):
    def get(self, request):
        about = AboutCompany.objects.first()
        about_data = AboutCompanySerializer(about).data

        timeline = CompanyTimeline.objects.all()
        timeline_data = CompanyTimelineSerializer(timeline, many=True).data

        return Response({
            "about": about_data,
            "timeline": timeline_data,
        })


class ManagerListView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)