from django.urls import path

from . import views
from . import views_auth
from . import views_super


urlpatterns = [

    # Authentication

    path(
        "login/",
        views_auth.user_login,
        name="login",
    ),

    path(
        "logout/",
        views_auth.user_logout,
        name="logout",
    ),
    
    # Suprident Dashboard

    path(
        "suprident-dashboard/",
        views_super.suprident_dashboard,
        name="suprident_dashboard",
    ),

    # Duty Assignemnt

    path(
        "suprident-dashboard/assign/",
        views_super.assign_duty,
        name="assign_duty",
    ),

    path(
        "suprident-dashboard/assign/auto/",
        views_super.auto_assign_monthly_duties,
        name="auto_assign_monthly_duties",
    ),

    path(
        "suprident-dashboard/generate-nfd/",
        views_super.generate_nfd_for_month,
        name="generate_nfd",
    ),

    path(
        "nfd/delete/<int:nfd_id>/",
        views_super.delete_nfd,
        name="delete_nfd",
    ),

    # DutyCRUD

    path(
        "suprident-dashboard/assign/save/",
        views_super.save_duty,
        name="save_duty",
    ),

    path(
        "suprident-dashboard/assign/edit/<int:duty_id>/",
        views_super.edit_duty_ajax,
        name="edit_duty_ajax",
    ),

    path(
        "suprident-dashboard/assign/delete/<int:duty_id>/",
        views_super.delete_duty_ajax,
        name="delete_duty_ajax",
    ),

    # Reports

    path(
        "suprident-dashboard/report/",
        views_super.generate_report,
        name="generate_report",
    ),

    path(
    'suprident-dashboard/report/pdf/',
    views_super.download_report_pdf,
    name='download_report_pdf'
    ),

path(
    'suprident-dashboard/report/word/',
    views_super.download_report_word,
    name='download_report_word'
), 

    # Employee Dashboard

    path(
        "employee-dashboard/",
        views.employee_dashboard,
        name="employee_dashboard",
    ),
]