from django.urls import path
from .views import UserInfoAPIView

urlpatterns = [
    path('user/', UserInfoAPIView.as_view()),
]
