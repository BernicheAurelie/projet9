import django.contrib.auth.models
from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    user = django.contrib.auth.models.User
