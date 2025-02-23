from django.urls import path, include
from . import views



urlpatterns = [
    path('data/',views.ResiverView.as_view()),
    path('data/<int:pk>',views.ResiverDataDetails.as_view()),
    
]