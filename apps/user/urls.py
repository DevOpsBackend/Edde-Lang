from django.urls import path
from .views import UserInfoAPIView, PaymentHistoryView, MyLanguageAPIView

urlpatterns = [
    path('user/', UserInfoAPIView.as_view()),
    path('payment-history/', PaymentHistoryView.as_view()),
    path('my-languages/', MyLanguageAPIView.as_view()),
]
