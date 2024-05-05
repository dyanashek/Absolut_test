from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from .forms import CustomUserForm
from .models import CustomUser


def login_or_signup(request):
    if request.method == 'GET':
        title = 'ERP | Absolut - система автоматизации'
        form = CustomUserForm
        template = 'users/login.html'
        context = {
            'title' : title,
            'form' : form,
        }
        return render(request, template, context)

    elif request.method == 'POST':
        if email := request.POST.get('email'):
            user = CustomUser.objects.get_or_create(email=email)[0]

            request.session['user_id'] = user.id
            
            success_url = reverse_lazy('questionnaire:questionnaire')
            
            return redirect(success_url)

        fail_url = reverse_lazy('users:login_or_signup')
        return redirect(fail_url)