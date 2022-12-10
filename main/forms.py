from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User
from .models import Talk, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}

class emailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email": "新しいメールアドレス"}
