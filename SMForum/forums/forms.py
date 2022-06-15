from django.contrib.auth.forms import UserChangeForm

from .models import Comment, User
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'nickname','studentId' ,'phoneNumber', 'my_image', 'github']
