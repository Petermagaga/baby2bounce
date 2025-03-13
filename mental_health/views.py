from rest_framework import generics,permissions
from .serializers import CounselingSessionSerializer,MotivationalMessageSerializer
from .models import CounselingSession,MotivationalMessage

class CounselingSessionView(generics.ListCreateAPIView):
    serializer_class = CounselingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CounselingSession.objects.filter(user=self.request.user).order_by('-session_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MotivationalMessageView(generics.ListAPIView):
    serializer_class = MotivationalMessageSerializer
    permission_classes = [permissions.AllowAny]
    queryset = MotivationalMessage.objects.all().order_by('-created_at')[:10]  # Latest 10 messages
