import schedule
from django import forms
from user.models import Comment

from . import models
from .models import employee_reg, work


class Comments(forms.ModelForm):
    #designation ="none"
    class Meta:
        model = Comment
        fields =['designation']
class employee_reg(forms.ModelForm):
    class Meta:
        model=employee_reg
        fields=['fname','email','designation','gender']
class Creatework(forms.ModelForm):

    class Meta:
        model = work
        fields =('message','fileToUpload','designation')
