"""Students models module"""

from django.db import models

# Utilities
from .users import User


class Student(models.Model):
    """Student user type class"""

    user = models.OneToOneField("User", on_delete=models.CASCADE)
