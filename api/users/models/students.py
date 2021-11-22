"""Students models module"""

from django.db import models

# Utilities
from .users import UserInfo


class Student(UserInfo):
    """Student user type class"""

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
