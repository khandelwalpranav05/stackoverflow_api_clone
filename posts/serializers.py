from rest_framework import serializers
from .models import Question, Answer, QuestionComment, AnswerComment


class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('id','text','created_by','created_at','question')


class AnswerSerializer(serializers.ModelSerializer):
    comments = AnswerCommentSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'created_by', 'created_at', 'comments', 'question')


class QuestionSerializer(serializers.ModelSerializer):
    comments = QuestionCommentSerializer(many=True, required=False)
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'created_by', 'created_at', 'comments', 'answers')
