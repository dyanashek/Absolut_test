from django.db import models

from questionnaire.models import Quiz, Question, Answer
from questionnaire.forms import MultipleChoiceForm, ChoiceForm, QuestionLongForm, QuestionShortForm


class CustomUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    joined_project = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    def get_forms_data(self):
        forms = sorted(self._get_all_forms(), key=lambda x: x.index_num)
        visible = []
        hidden = []
        
        for form in forms:
            if form.visible:
                visible.append(form.name)
            else:
                hidden.append(form.name)
        
        return forms, visible, hidden

    def _get_quizzes_forms(self):
        forms = []
        for quiz in Quiz.objects.all():
            if quiz.type == 'Choice':
                forms.append(ChoiceForm(quiz, self))
            elif quiz.type == 'MultipleChoice':
                forms.append(MultipleChoiceForm(quiz, self))
        
        return forms
    
    def _get_questions_forms(self):
        forms = []
        for question in Question.objects.all():
            if question.type == 'Long':
                forms.append(QuestionLongForm(question, self))
            elif question.type == 'Short':
                forms.append(QuestionShortForm(question, self))
        
        return forms

    def _get_all_forms(self):
        return self._get_questions_forms() + self._get_quizzes_forms()

    def save_changes(self, request):
        if answer_type := request.POST.get('type'):
            if answer_type == 'quiz':
                self._save_quiz(request)
            
            elif answer_type == 'question':
                self._save_question(request)
    
    def _save_quiz(self, request):
        quiz_id = request.POST.get('id')

        if quiz := Quiz.objects.filter(pk=quiz_id).first():
            choices = request.POST.getlist('choices')
            curr_quiz, create = Quiz_answer.objects.get_or_create(user = self, quiz = quiz)

            curr_quiz.answers.clear()
            for choice in choices:
                if answer := Answer.objects.filter(pk = int(choice)).first():
                    curr_quiz.answers.add(answer)
            
            curr_quiz.save()

    def _save_question(self, request):
        question_id = request.POST.get('id')

        if question := Question.objects.filter(pk=question_id).first():
            answer = request.POST.get('answer')
            curr_question, create = Question_answer.objects.get_or_create(user = self, question = question)
            curr_question.answer = answer
            curr_question.save()


class Quiz_answer(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name = 'quizzes_answers',
        on_delete=models.CASCADE,
    )
    quiz = models.ForeignKey(
        Quiz,
        blank=True,
        on_delete=models.CASCADE
    )
    answers = models.ManyToManyField(Answer)


class Question_answer(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name = 'questions_answers',
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        blank=True,
        on_delete=models.CASCADE
    )
    answer = models.TextField(max_length=1500)