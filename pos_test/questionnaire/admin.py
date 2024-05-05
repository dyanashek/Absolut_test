
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Question, Quiz, Answer


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        widgets = {
            'choices': FilteredSelectMultiple('Answers', is_stacked=False),
            'depends_on': FilteredSelectMultiple('Answers', is_stacked=False),
        }


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm
    list_display = ('pk', 'label', 'type', 'options', 'related', 'index_num',)
    list_editable = ('type', 'index_num',)
    search_fields = ('label',)
    empty_value_display = '-'

    def options(self, obj):
        if options := [str(choice.answer) for choice in obj.choices.all()]:
            return ', '.join(options)
        
        return None
    
    def related(self, obj):
        if related := [str(related.answer) for related in obj.depends_on.all()]:
            return related
        
        return None


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'answer',)
    list_editable = ('answer',)
    search_fields = ('answer',)
    

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'depends_on': FilteredSelectMultiple('Answers', is_stacked=False),
        }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('pk', 'question', 'type', 'related', 'index_num',)
    list_editable = ('type', 'index_num',)
    search_fields = ('question',)

    def related(self, obj):
        return ', '.join([str(related.answer) for related in obj.depends_on.all()])
