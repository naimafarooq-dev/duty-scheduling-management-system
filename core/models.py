from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from django.db.models import F, Q
from django.utils import timezone

# User & Employees

class User(models.Model):
    ROLE_CHOICES = (
        ("employee", "Employee"),
        ("suprident", "Superintendent"),
    )

    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    id = models.AutoField(primary_key=True)

    hr_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="HR Number",
        help_text="Unique HR identifier",
    )

    name = models.CharField(
        max_length=100,
        verbose_name="Full Name",
        help_text="Employee full name",
    )

    designation = models.CharField(
        max_length=100,
        verbose_name="Designation",
        help_text="Official job title",
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="employee",
        verbose_name="User Role",
        help_text="Whether user is Superintendent or Employee",
    )

    password = models.CharField(
        max_length=128,
        verbose_name="Password",
        help_text="Stored as a secure password hash",
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        verbose_name="Account Created At",
    )

    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="active",
        verbose_name="Account Status",
    )

    def set_password(self, raw_password):
        """Hash and store a password securely."""
        if not raw_password:
            raise ValueError("Password cannot be empty.")

        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check a raw password against the stored hash."""
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        """
        Automatically hash a password when a raw password is supplied.

        Existing Django password hashes are left unchanged.
        """
        if self.password:
            try:
                from django.contrib.auth.hashers import identify_hasher

                identify_hasher(self.password)
            except Exception:
                self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} [{self.hr_number}]"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["hr_number"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["role"]),
        ]

# NFDQueue

class NFDQueue(models.Model):
    DUTY_TYPES = [
        ("weekday", "Weekday"),
        ("weekend", "Weekend"),
    ]

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="nfd_entries",
        verbose_name="Employee",
        help_text="Employee scheduled for next duty",
    )

    assigned_id = models.CharField(
        max_length=50,
        verbose_name="Assigned ID",
        help_text="ID assigned during scheduling",
    )

    assigned_month = models.DateField(
        verbose_name="Assigned Month",
        help_text="Month this employee is expected for duty",
    )

    duty_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Duty Date",
        help_text="Exact duty date for this NFD entry",
    )

    duty_type = models.CharField(
        max_length=10,
        choices=DUTY_TYPES,
        verbose_name="Duty Type",
        help_text="Type of duty: Weekday or Weekend",
    )

    added_to_queue_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        verbose_name="Added To Queue",
        help_text="When employee was added to duty queue",
    )

    removed_from_queue_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Removed From Queue",
        help_text="When employee was removed from the queue",
    )

    def __str__(self):
        return f"{self.employee.name} → {self.duty_date} ({self.duty_type})"

    class Meta:
        verbose_name = "Next For Duty"
        verbose_name_plural = "NFD Queue"
        ordering = ["assigned_month", "duty_date"]
        indexes = [
            models.Index(fields=["assigned_month"]),
            models.Index(fields=["employee"]),
            models.Index(fields=["duty_date"]),
        ]

# Events

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ("fixed", "Fixed"),
        ("lunar", "Lunar"),
    ]

    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=100,
        verbose_name="Event Name",
        help_text="Name of the national or religious event",
    )

    date = models.DateField(
        verbose_name="Start Date",
        help_text="Start date of the event",
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="End Date",
        help_text="Leave blank for a single-day event",
    )

    event_type = models.CharField(
        max_length=10,
        choices=EVENT_TYPE_CHOICES,
        verbose_name="Event Type",
    )

    enabled = models.BooleanField(
        default=True,
        verbose_name="Is Active This Year?",
        help_text="Disabled events are ignored by scheduling",
    )

    is_weekend = models.BooleanField(
        default=False,
        verbose_name="Is Weekend?",
        help_text="Whether the event starts on a weekend",
    )

    def clean(self):
        """Validate event date range."""
        if self.end_date and self.end_date < self.date:
            raise ValidationError(
                {"end_date": "End date cannot be earlier than start date."}
            )

    def save(self, *args, **kwargs):
        # Automatically determine whether the start date is a weekend.
        self.is_weekend = self.date.weekday() >= 5

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.end_date:
            return f"{self.name} ({self.date} to {self.end_date})"

        return f"{self.name} ({self.date})"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["date"]
        indexes = [
            models.Index(fields=["date"]),
            models.Index(fields=["enabled"]),
            models.Index(fields=["event_type"]),
        ]

# Event Duty Record

class EventDutyRecord(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="event_duties",
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="duty_records",
    )

    duty_date = models.DateField()

    def __str__(self):
        event_name = self.event.name if self.event else "No Event"
        return f"{self.employee.name} on {self.duty_date} ({event_name})"

    class Meta:
        verbose_name = "Event Duty Record"
        verbose_name_plural = "Event Duty Records"
        ordering = ["duty_date", "employee__hr_number"]

        constraints = [
            models.UniqueConstraint(
                fields=["employee", "duty_date"],
                name="unique_employee_duty_date",
            ),
        ]

        indexes = [
            models.Index(fields=["duty_date"]),
            models.Index(fields=["employee"]),
            models.Index(fields=["event"]),
        ]