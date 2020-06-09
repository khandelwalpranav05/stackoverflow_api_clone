from posts.api.serializers import QuestionDetailSerializer, AnswerSerializer, QuestionCommentSerializer, \
    AnswerCommentSerializer, QuestionListSerializer
from posts.models import Question, Answer, QuestionComment, AnswerComment

from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


# Create your views here.

class QuestionListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionDetailSerializer
    serializer_action_classes = {
        'list': QuestionListSerializer
    }
    queryset = Question.objects.all()
    pagination_class = QuestionListPagination

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


class AnswerListView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs['id'])


class QuestionCommentListView(generics.ListCreateAPIView):
    serializer_class = QuestionCommentSerializer

    def get_queryset(self):
        return QuestionComment.objects.filter(question_id=self.kwargs['id'])


class QuestionCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionCommentSerializer
    queryset = QuestionComment.objects.all()
    lookup_field = 'id'


class AnswerCommentListView(generics.ListCreateAPIView):
    serializer_class = AnswerCommentSerializer

    def get_queryset(self):
        return AnswerComment.objects.filter(answer_id=self.kwargs['id'])


class AnswerCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerCommentSerializer
    queryset = AnswerComment.objects.all()
    lookup_field = 'id'
