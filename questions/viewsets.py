from rest_framework import viewsets

from .models import Question, Quiz
from .serializers import QuestionsSerializer, QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializer
    queryset = Question.objects.all()
