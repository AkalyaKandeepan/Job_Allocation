from django.contrib import auth
from django.db import connection
from django.shortcuts import render, redirect

# Create your views here.
#from adminpro.models import employee_reg
from adminpro.models import employee_reg
from user.models import Comment

from . import forms
from adminpro.models import work


def employee_index(request):
    return render(request, 'employee/employee_index.html')

def employee_com1(request):
    emp_id = request.session['eid']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    if Comment.objects.filter(designation__contains=emp_designation):
        return redirect("view_files1")
    else:
        return redirect("view_files1")


def employee_login(request):


        email = request.POST.get('email')
        group_password = request.POST.get('group_password')
        if request.method == "POST":
            employee_reg.objects.filter(email=email,group_password=group_password)
            check = employee_reg.objects.get(email=email, group_password=group_password)
            request.session['eid'] = check.id
            #request.session['ename'] = check.uname
            request.session['emp_email'] = check.email
            request.session['designation'] = check.designation
            return redirect('employee_com1')

        return render(request, 'employee/employee_login.html')




def view_files1(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    #emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)

    total_filedetails=Comment.objects.filter(designation__contains=emp_designation).exclude (report__lte='finish')



    return render(request, 'employee/view_files.html',{'objects': total_filedetails, 'emp_designation': emp_designation})




def com_view(request,id):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    # emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    com1=Comment.objects.get(id=id)

    return render(request, 'employee/viewcomment.html', {'com1': com1})
def report(request,id):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_email = request.session['emp_email']
    print(emp_id)
    emp_designation = request.session['designation']
    com1= Comment.objects.get(id=id)
    emp=Comment.objects.filter(id=id).update(emp_for=emp_id)
    print(emp)
    form = forms.Comments(request.POST, instance=com1)
    print(form)
    if form.is_valid():
        form.save()

        return redirect('view_files1')
    return render(request, 'employee/report.html', {'emp': com1})


#admin
def admin_com(request):
    emp_id = request.session['eid']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    if work.objects.filter(designation__contains=emp_designation):
        return redirect("view_files")
    else:
        return redirect("view_files")


def view_files(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    #emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)

    total_filedetails=work.objects.filter(designation__contains=emp_designation).exclude (report__lte='finish')


    return render(request, 'employee/admin_work.html',{'objects': total_filedetails, 'emp_designation': emp_designation})


def admin_view(request,id):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    # emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    com1=work.objects.get(id=id)

    return render(request, 'employee/viewadmincomment.html', {'com1': com1})


def project_report(request,id):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_email = request.session['emp_email']
    print(emp_id)
    emp_designation = request.session['designation']
    com1= work.objects.get(id=id)
    emp=work.objects.filter(id=id).update(emp_for=emp_id)
    print(emp)
    form = forms.admin_comments(request.POST, instance=com1)
    print(form)
    if form.is_valid():
        form.save()

        return redirect('view_files')
    return render(request, 'employee/adminreport.html', {'emp': com1})