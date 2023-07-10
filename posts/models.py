from django.contrib.auth.models import User, UserManager

from django.db import models
from django.utils.text import slugify
import jwt
from datetime import datetime, timedelta

from django.conf import settings


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


def create_user(self, username, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(username, email, password, **extra_fields)


@property
def token(self):
    token1 = jwt.encode(
        {'username': self.username, 'email': self.email,
         'exp': datetime.utcnow() + timedelta(hours=24)},
        settings.SECRET_KEY, algorithm='HS256')
    return token1
