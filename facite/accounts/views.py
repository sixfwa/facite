from django.shortcuts import render as _render, redirect as _redirect
from django.contrib import messages as _messages, auth as _auth

from . import forms as _forms

import services.account as _account


def create_account(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation_password = request.POST["confirmation_password"]

        if not _account.is_password_confirmation_password(
            password, confirmation_password
        ):
            _messages.error(request, "Passwords do not match")
            return _redirect("create-account")

        if _account.username_exists(username):
            _messages.error(request, "Username is already in use")
            return _redirect("create-account")

        if _account.email_exists(email):
            _messages.error(request, "Email is already in use")
            return _redirect("create-account")

        user = _account.create_user(username, password, email, first_name, last_name)

        _auth.login(request, user)

        return _redirect("index")

    return _render(
        request,
        "pages/authentication/create_account.html",
        {"form": _forms.CreateAccoutForm()},
    )


def logout(request):
    if request.method == "POST":
        _auth.logout(request)

    return _redirect("index")