from django.urls import path
from .views import HomeInfoView, SliderListView, MenuView

urlpatterns = [
    path("info/", HomeInfoView.as_view()),
    path("sliders/", SliderListView.as_view()),
    path("menu/", MenuView.as_view()),
]
