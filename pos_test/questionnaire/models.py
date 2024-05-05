from django.db import models

from core.choices.choices import QUIZ_TYPES, QUESTION_TYPES
from core.settings.settings import ANSWER_MAX_LENGTH, SHORT_ANSWER_MAX_LENGTH


class Answer(models.Model):
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()
    type = models.CharField(max_length=15, choices=QUESTION_TYPES)
    depends_on = models.ManyToManyField(Answer, blank=True, related_name='depends_questions')
    index_num = models.IntegerField(null=False)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    label = models.TextField(blank=True)
    type = models.CharField(max_length=ANSWER_MAX_LENGTH, choices=QUIZ_TYPES)
    choices = models.ManyToManyField(Answer, related_name='quizzes')
    depends_on = models.ManyToManyField(Answer, blank=True, related_name='depends_quizzes')
    index_num = models.IntegerField(null=False)

    def __str__(self):
        return self.label
