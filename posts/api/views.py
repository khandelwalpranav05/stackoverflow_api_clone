from posts.api.serializers import QuestionDetailSerializer, AnswerSerializer, QuestionCommentSerializer, \
    AnswerCommentSerializer,QuestionListSerializer
from posts.models import Question, Answer, QuestionComment, AnswerComment

from rest_framework import viewsets


# Create your views here.

class QuestionListViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionDetailSerializer
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
