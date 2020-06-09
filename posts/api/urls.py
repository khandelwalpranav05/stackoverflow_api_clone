from django.urls import path, include
from posts.api.views import QuestionViewSet, AnswerListView, QuestionCommentListView, QuestionCommentDetailView, \
    AnswerCommentListView, AnswerCommentDetailView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/<int:id>/comments', QuestionCommentListView.as_view()),
    path('question/<int:id>/answers', AnswerListView.as_view()),
    path('answer/<int:id>/comments', AnswerCommentListView.as_view()),
    path('question/comment/<int:id>', QuestionCommentDetailView.as_view()),
    path('answer/comment/<int:id>', AnswerCommentDetailView.as_view()),
]
