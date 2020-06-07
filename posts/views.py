from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer, QuestionCommentSerializer,AnswerCommentSerializer
from .models import Question, Answer, QuestionComment, AnswerComment

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


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


class AnswerCommentViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerCommentSerializer
    queryset = AnswerComment.objects.all()
