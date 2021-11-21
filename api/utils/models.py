"""Utils for models module"""

# Django
from django.db import models
from django.utils.translation import gettext as _


class TimeStampModel(models.Model):
    """TimeStamp abstract base model that provide to every table the
    created and updated dates.
    """

    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("Date time on which the object was created"),
    )

    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_("Date time on which the object was updated"),
    )

    class Meta:
        abstract = True
        get_latest_by = "created"
        ordering = ("-created_at", "-updated_at")
