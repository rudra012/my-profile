from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', null=True, blank=True)
    about = models.TextField(default='')

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.email = self.username
        super(User, self).save(*args, **kwargs)
