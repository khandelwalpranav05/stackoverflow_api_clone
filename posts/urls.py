from django.urls import path, include
from .views import QuestionViewSet, AnswerViewSet,QuestionCommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('questionComments',QuestionCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
