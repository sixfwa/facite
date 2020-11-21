from django.contrib.auth.models import User as _User


def is_password_confirmation_password(
    password: str, confirmation_password: str
) -> bool:
    return password == confirmation_password


def username_exists(username: str) -> bool:
    return _User.objects.filter(username=username).exists()


def email_exists(email: str) -> bool:
    return _User.objects.filter(email=email).exists()


def create_user(
    username: str, password: str, email: str, first_name: str, last_name: str
) -> _User:
    user = _User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    return user
