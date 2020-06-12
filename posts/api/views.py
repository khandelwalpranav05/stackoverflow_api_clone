from posts.api.serializers import QuestionDetailSerializer, AnswerSerializer, QuestionCommentSerializer, \
    AnswerCommentSerializer, QuestionListSerializer
from posts.models import Question, Answer, QuestionComment, AnswerComment

from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import filters
from rest_framework import permissions
# Create your views here.

from .permissions import IsOwnerOrReadOnly


class ListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionDetailSerializer
    serializer_action_classes = {
        'list': QuestionListSerializer
    }
    queryset = Question.objects.prefetch_related('created_by', 'comments').all()
    queryset_action = {
        'list': Question.objects.select_related('created_by').all()
    }
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = ListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        try:
            return self.queryset_action[self.action]
        except(KeyError, AttributeError):
            return super().get_queryset()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


class QuestionCommentListView(generics.ListCreateAPIView):
    serializer_class = QuestionCommentSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        queryset = QuestionComment.objects.select_related('created_by').filter(question_id=self.kwargs['id'])
        return queryset


class QuestionCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionCommentSerializer
    queryset = QuestionComment.objects.select_related('created_by').all()
    lookup_field = 'id'
    permission_classes = (IsOwnerOrReadOnly,)


class AnswerListView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return Answer.objects.prefetch_related('created_by', 'comments').filter(question_id=self.kwargs['id'])


class AnswerCommentListView(generics.ListCreateAPIView):
    serializer_class = AnswerCommentSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return AnswerComment.objects.select_related('created_by').filter(answer_id=self.kwargs['id'])


class AnswerCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerCommentSerializer
    queryset = AnswerComment.objects.select_related('created_by').all()
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
