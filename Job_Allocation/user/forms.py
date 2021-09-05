from django import forms
from user.models import Comment

from . import models


class CreateComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields =('message','fileToUpload')
