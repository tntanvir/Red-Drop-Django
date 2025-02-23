from django.urls import path, include
from . import views



urlpatterns = [
    path('data/',views.ReviewViews.as_view()),
    path('data/<int:id>/',views.ReviewDetailView.as_view()),
    
    
]