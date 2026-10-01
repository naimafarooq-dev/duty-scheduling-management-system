from django import forms

from .models import Event, User


class LoginForm(forms.Form):
    hr_number = forms.CharField(
        label="HR Number",
        max_length=20,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your HR number",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        max_length=128,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
            }
        ),
    )

    def clean_hr_number(self):
        hr_number = self.cleaned_data["hr_number"].strip()

        if not hr_number:
            raise forms.ValidationError("HR Number is required.")

        if not hr_number.isalnum():
            raise forms.ValidationError(
                "HR Number must contain only letters and numbers."
            )

        return hr_number


class AssignDutyForm(forms.Form):
    duty_date = forms.DateField(
        label="Duty Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": (
                    "border border-gray-300 rounded-lg p-2 w-full "
                    "focus:ring focus:ring-blue-300 focus:outline-none "
                    "transition"
                ),
            }
        ),
    )

    employee = forms.ModelChoiceField(
        label="Select Employee",
        queryset=User.objects.none(),
        widget=forms.Select(
            attrs={
                "class": (
                    "border border-gray-300 rounded-lg p-2 w-full "
                    "focus:ring focus:ring-blue-300 focus:outline-none "
                    "transition"
                ),
            }
        ),
    )

    event = forms.ModelChoiceField(
        label="Select Event (Optional)",
        queryset=Event.objects.none(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": (
                    "border border-gray-300 rounded-lg p-2 w-full "
                    "focus:ring focus:ring-blue-300 focus:outline-none "
                    "transition"
                ),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["employee"].queryset = (
            User.objects.filter(
                role="employee",
                status="active",
            )
            .order_by("name")
        )

        self.fields["event"].queryset = (
            Event.objects.filter(
                enabled=True,
            )
            .order_by("date")
        )