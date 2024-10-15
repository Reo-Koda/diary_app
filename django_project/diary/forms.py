from django.forms import ModelForm
from .models import Page
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ["title", "body", "picture"]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]