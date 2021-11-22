""" Users models module"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Utilities
from api.utils.models import TimeStampModel


class User(TimeStampModel, AbstractUser):
    """User auth model. Be careful about the info from AbstractUser
    Fields like first_name, last_name will be no used. User information
    will be handled for UserInfo model.
    """

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that username already exists.")},
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserInfo(TimeStampModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    father_last_name = models.CharField(
        _("father last name"), max_length=150, blank=True
    )
    mother_last_name = models.CharField(
        _("mother last name"), max_length=150, blank=True
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

    class Meta:
        abstract = True
