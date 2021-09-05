from user.models import Comment
from django import forms

from adminpro.models import work


class Comments(forms.ModelForm):

    class Meta:
        model = Comment
        fields =['report','emp']

class admin_comments(forms.ModelForm):

    class Meta:
        model = work
        fields =['report','emp']