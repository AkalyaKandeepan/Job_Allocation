from django.db import models
#import weekday_field
#from user.models import Comment


class employee_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    group_password = models.CharField(max_length=200)
    #user_com=models.ForeignKey(Comment,null=True,on_delete=models.CASCADE)
#admin comment
class work(models.Model):
    #actor = models.ForeignKey(User,on_delete=models.CASCADE)
    emp_for = models.ForeignKey(employee_reg,null=True,on_delete=models.CASCADE)

    message = models.TextField(max_length=2000)
    designation = models.TextField(max_length=2000,default="none")
    emp = models.TextField(max_length=2000,default="none")
    report = models.CharField(max_length=2000,default="none")
    fileToUpload = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.message


