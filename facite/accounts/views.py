from django.shortcuts import render as _render, redirect as _redirect
from django.contrib import messages as _messages

from . import forms as _forms

from services.account import (
    is_password_confirmation_password as _is_password_confirmation_password,
    username_exists as _username_exists,
    email_exists as _email_exists,
)


def create_account(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation_password = request.POST["confirmation_password"]

        if not _is_password_confirmation_password(password, confirmation_password):
            _messages.error(request, "Passwords do not match")
            return _redirect("create-account")

        if _username_exists(username):
            _messages.error(request, "Username is already in use")
            return _redirect("create-account")

        if _email_exists(email):
            _messages.error(request, "Email is already in use")
            return _redirect("create-account")

    return _render(
        request,
        "pages/authentication/create_account.html",
        {"form": _forms.CreateAccoutForm()},
    )
