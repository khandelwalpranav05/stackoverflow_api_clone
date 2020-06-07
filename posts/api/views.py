from posts.api.serializers import QuestionSerializer, AnswerSerializer, QuestionCommentSerializer, AnswerCommentSerializer
from posts.models import Question, Answer, QuestionComment, AnswerComment

from rest_framework import viewsets


# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class QuestionCommentViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionCommentSerializer
    queryset = QuestionComment.objects.all()


class AnswerCommentViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerCommentSerializer
    queryset = AnswerComment.objects.all()
