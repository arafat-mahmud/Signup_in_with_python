from django.db import models # type: ignore

from django.contrib.auth.hashers import make_password, check_password # type: ignore


class Sign_up_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Increased length for hashed passwords

    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        if not self.password.startswith(
            "pbkdf2_sha256$"
        ):  # Avoid re-hashing hashed passwords
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
