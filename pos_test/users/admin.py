from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CustomUser, Quiz_answer, Question_answer


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'joined_project', 'display_quizzes', 'display_answers')
    search_fields = ('answers',) 
    list_filter = ('joined_project',) 
    empty_value_display = '-нет ответов-'
    
    def display_quizzes(self, obj):
        display =''
        for answer in obj.quizzes_answers.all():
            if label := answer.quiz.label:
                display += f'{label}<br>'

            answers = answer.answers.all()
            answers_count = len(answers)
            if answers:
                for num, option in enumerate(answers):
                    display += f'&nbsp;{num + 1}. {option.answer}<br>'
                    if num == answers_count - 1:
                        display += '<br>'
            else:
                display += '-нет ответа-<br><br>'

        return mark_safe(display)
    
    def display_answers(self, obj):
        display =''
        for answer in obj.questions_answers.all():
            display += f'{answer.question}<br>{answer.answer}<br><br>'

        return mark_safe(display)

@admin.register(Quiz_answer)
class QuestionnaireQuizAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'quiz', 'display_answers',)

    def display_answers(self, obj):
        return ', '.join([str(answer.answer) for answer in obj.answers.all()])


@admin.register(Question_answer)
class QuestionnaireQuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'question', 'answer')