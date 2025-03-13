from django.urls import path
from .views import HealthProfileView,HealthRecommendationView

urlpatterns = [
    path('profile/', HealthProfileView.as_view(), name='health-profile'),
    path('recommendations/', HealthRecommendationView.as_view(), name='health-recommendations'),
]
