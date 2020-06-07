from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Manager

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class BaseComment(models.Model):
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class QuestionComment(BaseComment):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_comments')
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class AnswerComment(BaseComment):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_comments')
    answer = models.ForeignKey(Answer, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
