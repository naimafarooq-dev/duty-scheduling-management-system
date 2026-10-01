from django import forms
from django.contrib import admin

from .models import User, NFDQueue, Event, EventDutyRecord


# ============================================================
# User / Employee Admin Form
# ============================================================

class UserAdminForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "Enter password",
            }
        ),
        help_text=(
            "Enter a password for this account. "
            "The password will be stored securely as a hash."
        ),
    )

    class Meta:
        model = User
        fields = (
            "hr_number",
            "name",
            "designation",
            "role",
            "status",
            "password",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Password is required when creating a new user.
        if not self.instance.pk:
            self.fields["password"].required = True
            self.fields["password"].help_text = (
                "Enter the initial password for this account. "
                "It will be stored securely as a hash."
            )

    def save(self, commit=True):
        user = super().save(commit=False)

        raw_password = self.cleaned_data.get("password")

        # Set a new password only when:
        # 1. A new user is being created, or
        # 2. An existing user's password was entered/changed.
        if raw_password:
            user.set_password(raw_password)

        if commit:
            user.save()

        return user


# ============================================================
# Users / Employees
# ============================================================

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm

    list_display = (
        "hr_number",
        "name",
        "designation",
        "role",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "role",
        "designation",
    )

    search_fields = (
        "hr_number",
        "name",
        "designation",
    )

    ordering = ("hr_number",)

    save_on_top = True

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "User Information",
            {
                "fields": (
                    "hr_number",
                    "name",
                    "designation",
                    "role",
                    "status",
                ),
                "description": (
                    "Manage employee profile and account status."
                ),
            },
        ),
        (
            "Account Security",
            {
                "fields": (
                    "password",
                ),
                "description": (
                    "Set or change the employee's login password. "
                    "Passwords are stored securely and are never "
                    "displayed in plain text."
                ),
            },
        ),
        (
            "Account Information",
            {
                "fields": (
                    "created_at",
                ),
                "description": (
                    "Account creation information."
                ),
            },
        ),
    )


# ============================================================
# NFD Queue
# ============================================================

@admin.register(NFDQueue)
class NFDQueueAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "assigned_id",
        "assigned_month",
        "duty_type",
        "duty_date",
        "added_to_queue_at",
        "removed_from_queue_at",
    )

    list_filter = (
        "duty_type",
        "assigned_month",
    )

    search_fields = (
        "employee__name",
        "employee__hr_number",
        "assigned_id",
    )

    ordering = (
        "assigned_month",
        "added_to_queue_at",
    )

    readonly_fields = (
        "added_to_queue_at",
    )

    fieldsets = (
        (
            "Duty Assignment Details",
            {
                "fields": (
                    "employee",
                    "assigned_id",
                    "assigned_month",
                    "duty_type",
                    "duty_date",
                    "removed_from_queue_at",
                ),
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "added_to_queue_at",
                ),
            },
        ),
    )

    save_on_top = True


# ============================================================
# Events
# ============================================================

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "event_type",
        "date",
        "end_date",
        "enabled",
        "is_weekend",
    )

    list_filter = (
        "event_type",
        "enabled",
        "is_weekend",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "date",
        "name",
    )

    save_on_top = True


# ============================================================
# Event Duty Records
# ============================================================

@admin.register(EventDutyRecord)
class EventDutyRecordAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "event",
        "duty_date",
    )

    list_filter = (
        "event",
    )

    search_fields = (
        "employee__name",
        "employee__hr_number",
        "event__name",
    )

    ordering = (
        "duty_date",
        "employee__hr_number",
    )

    save_on_top = True
