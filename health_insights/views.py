
from rest_framework import generics,permissions
from django.shortcuts import render
from .models import HealthProfile,HealthRecommendation
from .serializers import HealthProfileSerializer,HealthRecommendationSerializer

import random

class HealthProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = HealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = HealthProfile.objects.get_or_create(user=self.request.user)
        return profile

class HealthRecommendationView(generics.ListCreateAPIView):
    serializer_class = HealthRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HealthRecommendation.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        user_profile = self.request.user.health_profile
        personalized_recommendation = generate_recommendation(user_profile)
        serializer.save(user=self.request.user, recommendation_text=personalized_recommendation)

def generate_recommendation(profile):
    recommendations = [
        "Maintain a balanced diet rich in proteins, vitamins, and minerals.",
        "Stay hydrated and drink at least 8 glasses of water daily.",
        "Engage in light exercises like prenatal yoga or walking.",
        "Get enough sleep to reduce stress and promote baby’s development."
    ]
    
    if "diabetes" in (profile.pre_existing_conditions or "").lower():
        recommendations.append("Monitor blood sugar levels and avoid high-sugar foods.")
    
    if "hypertension" in (profile.pre_existing_conditions or "").lower():
        recommendations.append("Reduce salt intake and practice relaxation techniques.")

    return random.choice(recommendations)

