from django.urls import path
from .views import CounselingSessionView,MotivationalMessageView

urlpatterns = [
    path('counseling/', CounselingSessionView.as_view(), name='counseling-sessions'),
    path('motivation/', MotivationalMessageView.as_view(), name='motivational-messages'),
]
