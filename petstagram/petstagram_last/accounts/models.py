from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_last.accounts.validators import validate_contains_alphabetical_letters
from petstagram_last.core.model_mixins import ChoiceEnumMixin


class Gender(ChoiceEnumMixin, Enum):
    male= 'Male'
    female= 'Female'
    doNotShow= 'Do not show'

print(Gender.choices())
for key,value in Gender.choices():
    print(value)
print(Gender.max_len())

# Create your models here.
class AppUser(AbstractUser):
    MIN_LEN_FIRST_NAME=2
    MAX_LEN_FIRST_NAME=30

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name= models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_contains_alphabetical_letters,
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_contains_alphabetical_letters
        ),
        null=True,
        blank=True
    )
    email= models.EmailField(
        unique=True,
        null=True,
        blank=True
    )
    gender= models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len()
    )