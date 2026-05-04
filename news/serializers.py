from rest_framework import serializers
from .models import News, NewsCategory


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name']

class NewsListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.name')

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'summary',
            'image',
            'published_at',
            'category',
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class NewsDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.name')

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'content',
            'image',
            'video',
            'link',
            'published_at',
            'category',
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_video(self, obj):
        request = self.context.get('request')
        if obj.video:
            return request.build_absolute_uri(obj.video.url)
        return None
