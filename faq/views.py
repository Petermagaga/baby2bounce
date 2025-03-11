from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import FAQSerializer,ExpertQuestionSerializer
from .models import FAQ,ExpertQuestion
from time import timezone

class FAQView(generics.ListAPIView):
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return FAQ.objects.filter(category=category)
        return FAQ.objects.all()

class ExpertQuestionView(generics.ListCreateAPIView):
    serializer_class = ExpertQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ExpertQuestion.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnswerExpertQuestionView(generics.UpdateAPIView):
    serializer_class = ExpertQuestionSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = ExpertQuestion.objects.all()

    def perform_update(self, serializer):
        serializer.save(answered_by=self.request.user, answered_at=timezone.now())
