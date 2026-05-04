from django.urls import path
from .views import (
    NewsandInsightsPageView,
    NewsDetailView,
    NewsCategoryListView,
)

urlpatterns = [
    path('news/', NewsandInsightsPageView.as_view()),
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('news/categories/', NewsCategoryListView.as_view()),
]
