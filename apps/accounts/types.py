import strawberry_django
from .models import CustomUser
from strawberry import auto


@strawberry_django.type(CustomUser)
class User:
    id: auto
    phone: auto
    email: auto
    first_name: auto
    last_name: auto
    is_active: auto
    is_staff: auto
    last_login: auto
    date_joined: auto
    full_name: auto
    is_anonymous: bool
    is_authenticated: bool


@strawberry_django.input(CustomUser)
class UserInput:
    phone: auto
    email: auto
    first_name: auto
    last_name: auto
    password: auto
