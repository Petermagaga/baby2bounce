from rest_framework import generics, permissions
from .serializers import ChatbotMessageSerializer
from .models import ChatbotMessage
import openai

# Set OpenAI API key globally
openai.api_key = "your_api_key_here"


class ChatbotView(generics.CreateAPIView):
    serializer_class = ChatbotMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_message = serializer.validated_data['message']
        ai_response = generate_chatbot_response(user_message)
        serializer.save(user=self.request.user, response=ai_response)


def generate_chatbot_response(user_message):
    # Simple predefined response system (replace with AI integration if needed)
    responses = {
        "morning sickness": "Morning sickness is common in early pregnancy. Try eating small meals and staying hydrated.",
        "prenatal vitamins": "Taking folic acid and iron supplements is important for a healthy pregnancy.",
        "labor pain": "Labor pain is natural. Practice breathing exercises and prepare for different pain relief options.",
    }

    # Check for keyword-based response
    for keyword, response in responses.items():
        if keyword in user_message.lower():
            return response

    # If no predefined answer, generate AI response
    return call_ai_model(user_message)


def call_ai_model(user_message):
    client = openai.OpenAI(api_key="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")  # Ensure your API key is correct

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Change from "gpt-4" to "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful pregnancy health assistant."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()