from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)

    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
