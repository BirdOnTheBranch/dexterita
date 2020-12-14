from rest_framework import serializers

from .models import Date, Question, Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('month', 'year', 'model')


class QuestionsSerializer(serializers.ModelSerializer):
    date = DateSerializer()

    class Meta:
        model = Question
        fields = ('text', 'date', 'responses')
