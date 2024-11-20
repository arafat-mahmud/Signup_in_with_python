from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from .models import Sign_up_form
from .forms import SignUpForm


# Sign-up view
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign-up successful! You can now log in.")
            return redirect("login")
        else:
            # Collect form error details
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            # messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


# Login view
from django.contrib.auth.hashers import check_password  # type: ignore


def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email:
            messages.error(request, "Email is required.")
        elif not password:
            messages.error(request, "Password is required.")
        else:
            try:
                user = Sign_up_form.objects.get(email=email)
                if check_password(password, user.password):
                    request.session["user_id"] = user.id
                    return redirect("welcome")
                else:
                    messages.error(request, "Invalid password.")
            except Sign_up_form.DoesNotExist:
                messages.error(request, "No user found with this email.")

    return render(request, "login.html")


# Welcome view
def welcome(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = Sign_up_form.objects.get(id=user_id)
    return render(request, "welcome.html", {"user": user})


# Logout view
def logout_view(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "You have been logged out.")
    return redirect("login")
