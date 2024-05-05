from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse

from users.models import CustomUser, Question_answer, Quiz_answer
from .models import Quiz, Question, Answer
from .forms import MultipleChoiceForm, ChoiceForm, QuestionShortForm, QuestionLongForm


def questionnaire(request): 
    if user_id := request.session.get('user_id'):
        user = CustomUser.objects.filter(id = user_id).first()

        if user:
            user.save_changes(request)
            forms, visible, hidden = user.get_forms_data()
            
            if request.POST.get('type'):
                data = {
                    'visible' : visible,
                    'hidden' : hidden,
                }
                return JsonResponse(data)

            title = 'ERP | Absolut - система автоматизации'
            template = 'questionnaire/questionnaire.html'
            context = {
                'title' : title,
                'email' : user.email,
                'forms' : forms,
                'visible' : visible,
            }

            return render(request, template, context)

    fail_url = reverse_lazy('users:login_or_signup')
    return redirect(fail_url)