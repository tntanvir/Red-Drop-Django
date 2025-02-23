# urls.py
from django.urls import path
from .views import CreateDonationRequestView

urlpatterns = [
    path('api/donate/', CreateDonationRequestView.as_view(), name='create-donation-request'),
]
