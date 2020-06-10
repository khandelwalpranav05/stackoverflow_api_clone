from rest_framework import serializers
from posts.models import Question, Answer, QuestionComment, AnswerComment
from accounts.api.serializers import UserBasicSerializer


class QuestionListSerializer(serializers.ModelSerializer):
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'created_at', 'created_by')


class QuestionDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'created_by', 'created_at', 'comments')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return Question.objects.create(**validated_data, created_by=user)

    def get_comments(self, instance):
        return QuestionCommentSerializer(instance.comments.all()[:2], many=True).data


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
        return QuestionComment.objects.create(**validated_data, created_by=user)


class AnswerSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    created_by = UserBasicSerializer(required=False)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'created_by', 'created_at', 'comments', 'question')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_by': {'read_only': True},
            'created_at': {'read_only': True},
            'comments': {'read_only': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return Answer.objects.create(**validated_data, created_by=user)

    def get_comments(self, instance):
        return AnswerCommentSerializer(instance.comments.all()[:1], many=True).data


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
