"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from user import views
from adminpro import views as adminproviews
from employee import views as employeeviews


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^register/$',views.register, name="register"),
    url(r'^$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^com/$', views.com, name="com"),

    url(r'^admin_main/$', adminproviews.main, name="admin_main"),
    url(r'^projectadmin_login/$', adminproviews.projectadmin_login, name="projectadmin_login"),
    url(r'^employee_com/$', adminproviews.employee_com, name="employee_com"),
    path('emp_com/<int:id>', adminproviews.emp_com, name="emp_com"),
    #path('emp_update/<int:id>', adminproviews.emp_update, name="emp_update"),
    path('delete_view/<int:id>', adminproviews.delete_view, name="delete_view"),
    path('delete_admin/<int:id>', adminproviews.delete_admin, name="delete_admin"),
    path('delete_admin_report/<int:id>', adminproviews.delete_admin_report, name="delete_admin_report"),

    url(r'employee_register/$',adminproviews.employee_register,name="employee_register"),
    url(r'logout_admin/$',adminproviews.logout_admin,name="logout_admin"),
    url(r'user_details/$',adminproviews.user_details,name="user_details"),
    url(r'project_reports/$',adminproviews.project_reports,name="project_reports"),
    url(r'adminreports/$',adminproviews.adminreports,name="adminreports"),
    url(r'work/$',adminproviews.works,name="work"),


    url(r'employee_login/$',employeeviews.employee_login,name="employee_login"),
    url(r'employee_details/$',adminproviews.employee_details,name="employee_details"),
    url(r'employee_com1/$',employeeviews.employee_com1,name="employee_com1"),
    url(r'view_files1/$',employeeviews.view_files1,name="view_files1"),
    url(r'employee_index/$',employeeviews.employee_index,name="employee_index"),
    url(r'view_files/$',employeeviews.view_files,name="view_files"),
    path('com_view/<int:id>',employeeviews.com_view,name="com_view"),
    path('admin_view/<int:id>',employeeviews.admin_view,name="admin_view"),
    path('report/<int:id>',employeeviews.report,name="report"),
    path('project_report/<int:id>',employeeviews.project_report,name="project_report"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)