from django.urls import path
from .views import AboutPageView, ManagerListView

urlpatterns = [
    path("", AboutPageView.as_view()),
]
