from django.core.exceptions import ValidationError


def validate_contains_alphabetical_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Only letters are allowed.")