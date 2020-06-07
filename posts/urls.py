from django.urls import path, include
from .views import QuestionViewSet, AnswerViewSet,QuestionCommentViewSet,AnswerCommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('questionComments',QuestionCommentViewSet)
router.register('answerComments',AnswerCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
