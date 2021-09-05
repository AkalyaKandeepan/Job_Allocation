from datetime import datetime

from Tools.scripts.texi2html import increment
from django.db import models
from django.contrib.auth.models import User
from adminpro.models import employee_reg

class Comment(models.Model):
    Report=(
        ('pending','pending'),
        ('finish','finish'),
    )
    actor = models.ForeignKey(User,on_delete=models.CASCADE)
    emp_for = models.ForeignKey(employee_reg,null=True,on_delete=models.CASCADE)
    #dob = models.DateTimeField(default=datetime.now, blank=True)
    message = models.TextField(max_length=2000)
    designation = models.TextField(max_length=2000,default="none")
    emp = models.TextField(max_length=2000,default="none")
    report = models.CharField(max_length=2000,null=True,choices=Report)
    fileToUpload = models.ImageField(upload_to='media/',default='None')

    def __str__(self):
        return self.message

