from rest_framework import serializers
from .models import Question, Answer, QuestionComment, AnswerComment

class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        fields = '__all__'

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    comments = AnswerCommentSerializer(many=True)
    class Meta:
        model = Answer
        fields = ('id','text','created_by','created_at','comments')


class QuestionSerializer(serializers.ModelSerializer):
    comments = QuestionCommentSerializer(many=True)
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id','title','description','created_by','created_at','comments','answers')
