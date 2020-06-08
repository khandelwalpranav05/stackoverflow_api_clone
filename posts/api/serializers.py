from rest_framework import serializers
from posts.models import Question, Answer, QuestionComment, AnswerComment
from accounts.api.serializers import UserBasicSerializer


class AnswerCommentSerializer(serializers.ModelSerializer):
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = AnswerComment
        fields = ('id', 'text', 'created_by', 'created_at', 'answer')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return AnswerComment.objects.create(**validated_data, created_by=user)


class QuestionCommentSerializer(serializers.ModelSerializer):
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = QuestionComment
        fields = ('id', 'text', 'created_by', 'created_at', 'question')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return AnswerComment.objects.create(**validated_data, created_by=user)


class AnswerSerializer(serializers.ModelSerializer):
    comments = AnswerCommentSerializer(many=True, required=False)
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'created_by', 'created_at', 'comments', 'question')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return AnswerComment.objects.create(**validated_data, created_by=user)


class QuestionDetailSerializer(serializers.ModelSerializer):
    comments = QuestionCommentSerializer(many=True, required=False)
    answers = AnswerSerializer(many=True, required=False)
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'created_by', 'created_at', 'comments', 'answers')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return Question.objects.create(**validated_data, created_by=user)


class QuestionListSerializer(serializers.ModelSerializer):
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'created_at', 'created_by')
