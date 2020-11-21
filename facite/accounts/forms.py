from django import forms as _forms


class CreateAccoutForm(_forms.Form):

    first_name = _forms.CharField(
        widget=_forms.TextInput(attrs={"placeholder": "First Name"}),
    )

    last_name = _forms.CharField(
        widget=_forms.TextInput(attrs={"placeholder": "Last Name"})
    )

    username = _forms.CharField(
        widget=_forms.TextInput(attrs={"placeholder": "Username"})
    )

    email = _forms.EmailField(
        widget=_forms.EmailInput(attrs={"placeholder": "Email"}),
    )

    password = _forms.CharField(
        widget=_forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    confirmation_password = _forms.CharField(
        widget=_forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )


class LoginForm(_forms.Form):

    username = _forms.CharField(
        widget=_forms.TextInput(attrs={"placeholder": "Username"})
    )

    password = _forms.CharField(
        widget=_forms.PasswordInput(attrs={"placeholder": "Password"})
    )