from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import News, NewsCategory
from .serializers import NewsListSerializer, NewsCategorySerializer, NewsDetailSerializer

class NewsandInsightsPageView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category')

        news_qs = News.objects.order_by('-published_at')

        if category_id:
            news_qs = news_qs.filter(category_id=category_id)

        featured = news_qs.first()
        others = news_qs[1:]

        return Response({
            "featured": NewsListSerializer(
                featured,
                context={'request': request}
            ).data if featured else None,

            "news": NewsListSerializer(
                others,
                many=True,
                context={'request': request}
            ).data,
        })


class NewsDetailView(APIView):
    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)

        return Response(
            NewsDetailSerializer(
                news,
                context={'request': request}
            ).data
        )

class NewsCategoryListView(APIView):
    def get(self, request):
        categories = NewsCategory.objects.all()
        return Response(
            NewsCategorySerializer(categories, many=True).data
        )