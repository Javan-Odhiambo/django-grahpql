from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)
