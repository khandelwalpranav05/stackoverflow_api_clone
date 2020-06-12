import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackoverflow_api_clone.settings')

import django

django.setup()

import random
from posts.models import Question, QuestionComment, Answer, AnswerComment
from django.contrib.auth import get_user_model

User = get_user_model()

from faker import Faker

fakegen = Faker()

usernames = ['Raghav Sharma', 'Yadnesh Sawant', 'Puneet Gupta', 'Parth Saluja', 'Sahib Thukral', 'Lalit Saini',
             'Vatsal Juneja', 'Vaudev Singh']

second_usernames = ['Surbhi Sardana', 'Aayush Sharma', 'Dharang Sharma', 'Himanshu Shankar', 'Ajay Khandelwal',
                    'Sanket Singh', 'Anshul Dhawan', 'Ram Sangwan', 'Siddhant Tyagi', 'Rohit Bhardwaj']


def get_user():
    user = User.objects.get_or_create(username=random.choice(usernames), password='khandelwalpranav')[0]
    user.save()
    return user


def second_user():
    user = User.objects.get_or_create(username=random.choice(second_usernames), password='khandelwalpranav')[0]
    user.save()
    return user


def gen_user(N):
    for i in range(N):
        fake_name = fakegen.name()
        user = User.objects.get_or_create(username=fake_name, password='khandelwalpranav')[0]
        user.save()
        return user


def gen_questons(N=100):
    users = User.objects.all()
    for i in range(N):
        user = random.choice(users)
        fake_title = fakegen.sentence()
        fake_description = fakegen.text()
        question = Question.objects.get_or_create(title=fake_title, description=fake_description, created_by=user)[0]
        question.save()


def gen_answer(N=300):
    users = User.objects.all()
    questions = Question.objects.all()
    for i in range(N):
        user = random.choice(users)
        fake_text = fakegen.sentence()
        random_question = random.choice(questions)
        answer = Answer.objects.get_or_create(text=fake_text, question=random_question, created_by=user)[0]
        answer.save()


def gen_question_comment(N=400):
    questions = Question.objects.all()
    users = User.objects.all()

    for i in range(N):
        user = random.choice(users)
        fake_text = fakegen.sentence()
        random_question = random.choice(questions)
        question_comment = QuestionComment.objects.get_or_create(text=fake_text, question=random_question,
                                                                 created_by=user)[0]
        question_comment.save()


def gen_answer_comment(N=1000):
    users = User.objects.all()
    answers = Answer.objects.all()
    for i in range(N):
        user = random.choice(users)
        fake_text = fakegen.sentence()
        random_answer = random.choice(answers)
        answer_comment = AnswerComment.objects.get_or_create(text=fake_text, answer=random_answer,
                                                             created_by=user)[0]
        answer_comment.save()


def populating(N=1000):
    user_count = N
    # question_count = N
    answer_count = 4 * N
    question_comment_count = 4 * N
    answer_comment_count = 10 * N
    gen_user(user_count)
    print('User Done')
    # gen_questons(question_count)
    # print('Questions Done')
    # gen_answer(answer_count)
    # print('Answer Done')
    gen_question_comment(question_comment_count)
    print('Question Comment Done')
    gen_answer_comment(answer_comment_count)
    print('Answer Comment Done')


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populating(10000)
    print('Populating Complete')
