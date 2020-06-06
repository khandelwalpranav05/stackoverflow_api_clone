from django.shortcuts import render
from .serializers import QuestionSerializer,AnswerSerializer,QuestionCommentSerializer
from .models import Question,Answer,QuestionComment,AnswerComment

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


class QuestionCommentViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionCommentSerializer
    queryset = QuestionComment.objects.all()