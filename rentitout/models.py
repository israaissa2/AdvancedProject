from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    role = models.PositiveSmallIntegerField(choices=[
        (1, "USER"), (2, "TEACHER"), (3, "TRAINER"), (4, "ADMIN")
    ], default=1)

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', True)  # Extract commit if passed
        super(User, self).save(*args, **kwargs)  # Pass the rest of kwargs
        if commit:
            super(User, self).save(*args, **kwargs)
        return self

