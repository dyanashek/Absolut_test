from django import forms

from .models import Quiz, Question
from core.settings.settings import ANSWER_MAX_LENGTH, SHORT_ANSWER_MAX_LENGTH


class QuizBaseForm(forms.Form):
    def __init__(self, quiz: Quiz, user, *args, **kwargs):
        super(QuizBaseForm, self).__init__(*args, **kwargs)

        self.user = user
        self.quiz = quiz
        self.id = quiz.pk
        self.name = f'quiz_{quiz.pk}'
        self.type = 'quiz'
        self.visible = self._set_visibility()
        self.index_num = quiz.index_num

    def _get_choices(self):
        choices = []
        for choice in self.quiz.choices.all():
            choices.append((choice.pk, choice.answer,))
        
        return choices

    def _get_initial(self):
        if answers := self.user.quizzes_answers.all().filter(quiz = self.quiz).first():
            answers_ids = []
            for answer in answers.answers.all():
                answers_ids.append(answer.pk)

            return answers_ids

        return None

    def _set_visibility(self):
        visible = False

        if not self.quiz.depends_on.first():
            visible = True
        else:
            users_answers = set()
            for quiz_answers in self.user.quizzes_answers.all():
                users_answers.update(quiz_answers.answers.all())
            
            for answer in self.quiz.depends_on.all():
                if answer in users_answers:
                    visible = True
                    break
        
        return visible


class MultipleChoiceForm(QuizBaseForm):
    def __init__(self, *args, **kwargs):
        super(MultipleChoiceForm, self).__init__(*args, **kwargs)

        self.fields['choices'] = forms.MultipleChoiceField(
            required=False, 
            label=self.quiz.label, 
            choices=self._get_choices(), 
            widget=forms.widgets.CheckboxSelectMultiple,
            initial=self._get_initial(),
            )


class ChoiceForm(QuizBaseForm):
    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)

        self.fields['choices'] = forms.ChoiceField(
            required=False, 
            label=self.quiz.label, 
            choices=self._get_choices(), 
            widget=forms.widgets.RadioSelect,
            initial=self._get_initial(),
            )


class QuestionBaseForm(forms.Form):
    def __init__(self, question: Question, user, *args, **kwargs):
        super(QuestionBaseForm, self).__init__(*args, **kwargs)

        self.user = user
        self.question = question
        self.id = question.pk
        self.name = f'question_{question.pk}'
        self.type = 'question'
        self.visible = self._set_visibility()
        self.index_num = question.index_num

    def _get_initial(self):
        if question := self.user.questions_answers.all().filter(question = self.question).first():
            return question.answer
        
        return None
    
    def _set_visibility(self):
        visible = False

        if not self.question.depends_on.first():
            visible = True
        else:
            users_answers = set()
            for quiz_answer in self.user.quizzes_answers.all():
                users_answers.update(quiz_answer.answers.all())
            
            for answer in self.question.depends_on.all():
                if answer in users_answers:
                    visible = True
                    break
        
        return visible


class QuestionShortForm(QuestionBaseForm):
    def __init__(self, *args, **kwargs):
        super(QuestionShortForm, self).__init__(*args, **kwargs)

        self.fields['answer'] = forms.CharField(
            max_length=SHORT_ANSWER_MAX_LENGTH,
            label=self.question.question,
            initial=self._get_initial(),
            )


class QuestionLongForm(QuestionBaseForm):
    def __init__(self,  *args, **kwargs):
        super(QuestionLongForm, self).__init__(*args, **kwargs)

        self.fields['answer'] = forms.CharField(
            widget=forms.widgets.Textarea, 
            max_length=ANSWER_MAX_LENGTH,
            label=self.question.question,
            initial=self._get_initial(),
            )