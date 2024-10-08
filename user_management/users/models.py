from django.db import models
from django.core.validators import EmailValidator, RegexValidator, MinLengthValidator, MaxLengthValidator

class User(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2, "First name must be at least 2 characters long.")]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2, "Last name must be at least 2 characters long.")]
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    address = models.TextField(
        validators=[MinLengthValidator(10, "Address must be at least 10 characters long.")]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
