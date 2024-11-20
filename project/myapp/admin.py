from django.contrib import admin # type: ignore

from django.contrib import admin # type: ignore
from .models import Sign_up_form


@admin.register(Sign_up_form)
class SignUpFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password")  # Columns displayed in the admin


# Register your models here.
# user: abc
# pass: abc
