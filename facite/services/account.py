from django.contrib.auth.models import User as _User


def is_password_confirmation_password(
    password: str, confirmation_password: str
) -> bool:
    return password == confirmation_password


def username_exists(username: str) -> bool:
    return _User.objects.filter(username=username).exists()


def email_exists(email: str) -> bool:
    return _User.objects.filter(email=email).exists()