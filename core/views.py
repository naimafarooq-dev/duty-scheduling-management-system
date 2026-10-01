from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.timezone import now

from .models import EventDutyRecord


def employee_dashboard(request):
    """
    Display the current month's duties for the logged-in employee.
    """

    user_id = request.session.get("user_id")
    role = request.session.get("role")

    if not user_id or role != "employee":
        messages.error(
            request,
            "You are not authorized to view this page.",
        )
        return redirect("login")

    current_date = now()

    my_duties = (
        EventDutyRecord.objects
        .select_related("employee", "event")
        .filter(
            employee_id=user_id,
            duty_date__year=current_date.year,
            duty_date__month=current_date.month,
        )
        .order_by("duty_date")
    )

    return render(
        request,
        "core/employee/dashboard.html",
        {
            "my_duties": my_duties,
            "month": current_date.strftime("%B %Y"),
        },
    )