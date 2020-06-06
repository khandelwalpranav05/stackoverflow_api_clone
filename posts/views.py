from django.shortcuts import render
from .serializers import QuestionSerializer,AnswerSerializer
from .models import Question,Answer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()