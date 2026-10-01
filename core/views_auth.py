from django.contrib import messages
from django.shortcuts import redirect, render

from .models import User


def user_login(request):
    """
    Authenticate Superintendent and Employee users
    using HR Number and hashed password.
    """

    if request.method == "POST":
        hr_number = request.POST.get("hr_number", "").strip()
        password = request.POST.get("password", "")

        if not hr_number or not password:
            messages.error(request, "HR number and password are required.")
            return render(request, "core/login.html")

        try:
            user = User.objects.get(hr_number=hr_number)
        except User.DoesNotExist:
            messages.error(request, "Invalid HR number or password.")
            return render(request, "core/login.html")

        # Do not allow inactive users to log in.
        if user.status != "active":
            messages.error(request, "This account is inactive.")
            return render(request, "core/login.html")

        # Verify the hashed password.
        if not user.check_password(password):
            messages.error(request, "Invalid HR number or password.")
            return render(request, "core/login.html")

        # Clear any existing session data before creating
        # a new authenticated session.
        request.session.flush()

        request.session["user_id"] = user.id
        request.session["role"] = user.role
        request.session["name"] = user.name

        # Redirect according to the user's role.
        if user.role == "suprident":
            return redirect("suprident_dashboard")

        return redirect("employee_dashboard")

    return render(request, "core/login.html")


def user_logout(request):
    """Log the current user out by clearing the session."""
    request.session.flush()
    return redirect("login")