from django.db.models import Q

from ..models import Event


def get_events_for_date(duty_date):
    """
    Return all active events that occur on the given date.

    Supports:
    - Single-day events
    - Multi-day events
    - Multiple events on the same date
    """

    return Event.objects.filter(
        enabled=True,
        date__lte=duty_date,
    ).filter(
        Q(
            end_date__isnull=True,
            date=duty_date,
        )
        |
        Q(
            end_date__isnull=False,
            end_date__gte=duty_date,
        )
    ).order_by("date", "name")
