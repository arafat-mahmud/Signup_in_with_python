from django import forms  # type: ignore
from .models import Sign_up_form


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    class Meta:
        model = Sign_up_form
        fields = ["name", "email", "password"]
        widgets = {
            "password": forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Sign_up_form.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already registered. Please try another."
            )
        return email
