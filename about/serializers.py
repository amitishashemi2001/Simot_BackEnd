from rest_framework import serializers
from .models import AboutCompany, CompanyTimeline, Manager

class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = '__all__'

class CompanyTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTimeline
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'