from django.urls import path, include
from posts.api.views import QuestionViewSet, AnswerViewSet,QuestionCommentViewSet,AnswerCommentViewSet,QuestionListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questionDetails', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('questionComments',QuestionCommentViewSet)
router.register('answerComments',AnswerCommentViewSet)
router.register('questions',QuestionListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]