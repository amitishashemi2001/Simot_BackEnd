from rest_framework import serializers
from .models import SiteInfo, Slider

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = ['logo', 'about_text', 'successful_projects']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'image', 'title', 'description']
