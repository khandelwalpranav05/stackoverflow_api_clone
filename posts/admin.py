from django.contrib import admin
from .models import Question,QuestionComment,Answer,AnswerComment

# Register your models here.

admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(Answer)