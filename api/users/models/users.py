""" Users models module"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Utilities
from api.utils.models import TimeStampModel


class User(TimeStampModel, AbstractUser):

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that username already exists.")},
    )
    phone_number = models.CharField(_("user phone number"), max_length=17, blank=True)
    cel_phone_number = models.CharField(
        _("user cel phone number"), max_length=17, blank=True
    )
    street_address = models.CharField(
        _("street user address"), max_length=255, blank=True
    )
    colony_address = models.CharField(
        _("colony user address"), max_length=255, blank=True
    )

    cp_address = models.CharField(
        _("cp address"),
        max_length=8,
        blank=True,
    )
    city_address = models.CharField(_("city user address"), max_length=255, blank=True)
    country_address = models.CharField(
        _("country user address"), max_length=20, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
