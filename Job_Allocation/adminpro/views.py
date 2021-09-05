import time

import schedule
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from user.models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import Creatework
from .models import employee_reg, work

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
from datetime import date



def main(request):
    return render(request,'projectadmin/home.html')
def projectadmin_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        if uname == 'admin' and password == 'admin':
            return redirect("work")
    return render(request, 'projectadmin/login.html')

def logout_admin(request):
    logout(request)
    return redirect('projectadmin_login')

def employee_com(request):
    if 'q1' in request.GET:
        q1=request.GET['q1']
        Comment.objects.filter(designation__icontains=q1)


    else:
        emp=Comment.objects.filter(designation='none')
        page = request.GET.get('page', 1)
        paginator = Paginator(emp, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'projectadmin/sharecom.html',{'users':users})
# Create your views here.
def emp_com(request,id):
    emp=Comment.objects.get(id=id)
    form = forms.Comments(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('employee_com')
    return render(request, 'projectadmin/allocate.html', {'emp': emp})




def delete_view(request,id):
    context = {}
    obj = get_object_or_404(employee_reg, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("employee_details")

    return render(request, "projectadmin/delete_view.html", context)




def employee_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        if designation=="Cleaning":
            group_password="SEE004"
        elif designation=="electricity_maintenance":
            group_password = "JEE101"
        elif designation == "ops_Security":
            group_password = "OPS203"
        elif designation == "ac_service":
            group_password = "ACS899"
        elif designation == "plumbing":
            group_password = "PLU987"
        elif designation == "gardening":
            group_password = "GAR900"
        elif designation == "internet":
            group_password = "INT876"
        else:
            group_password = "DGMP987"

        subject = "Group Password"
        text_content = ""

        html_content = "<br/><p>Your Group Password Is:<strong>" + str(group_password) + "<strong></p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            employee_reg.objects.create(fname=first_name, lname=last_name, email=email, designation=designation, gender=gender,group_password=group_password)
        return redirect('employee_register')
    return render(request, 'projectadmin/employee_reg.html')


def employee_details(request):
    employee_details = employee_reg.objects.all()
    return render(request, 'projectadmin/employee_details.html',{'employee_details':employee_details})

def user_details(request):
    users=User.objects.all()
    return render(request,'projectadmin/user_details.html',{'users':users})
def project_reports(request):
    if 'q' in request.GET:
        q=request.GET['q']
        emp = Comment.objects.filter(report__icontains=q)
        print(q)
        #return redirect('/project_reports')
    else:
        report1=Comment.objects.filter(report__isnull=False)
        page = request.GET.get('page', 1)
        paginator = Paginator(report1, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    return render(request,'projectadmin/report_emp.html',{'report':users})



#admin create comment

def works(request):
    saved = False
    if request.method=='POST':
        form=Creatework(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            saved = True
            return redirect('work')

    else:
        form=Creatework()
    return render(request,'projectadmin/work.html',{'form':form})

def adminreports(request):
    if 'q' in request.GET:
        q=request.GET['q']
        report = work.objects.filter(report__icontains=q)
    else:
        report=work.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(report, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,'projectadmin/admin_report_emp.html',{'report':users})



def delete_admin(request,id):
    context = {}
    obj = get_object_or_404(Comment, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("project_reports")

    return render(request, "projectadmin/delete_work.html", context)

def delete_admin_report(request,id):
    context = {}
    obj = get_object_or_404(work, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("adminreports")

    return render(request, "projectadmin/delete_admin_work.html", context)



