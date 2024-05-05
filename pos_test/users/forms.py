from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',) 