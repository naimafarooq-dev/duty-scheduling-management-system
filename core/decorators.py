from functools import wraps

from django.shortcuts import redirect

from .models import User


def role_required(role):
    """
    Restrict a view to authenticated users with a specific role.
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            user_id = request.session.get("user_id")

            # User is not logged in
            if not user_id:
                return redirect("login")

            try:
                user = User.objects.get(
                    id=user_id,
                    status="active",
                )
            except User.DoesNotExist:
                request.session.flush()
                return redirect("login")

            # Verify role from database instead of trusting
            # the role stored in the session.
            if user.role != role:
                return redirect("login")

            # Keep session information synchronized
            request.session["user_id"] = user.id
            request.session["name"] = user.name
            request.session["role"] = user.role

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator