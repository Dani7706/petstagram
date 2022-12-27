from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_last.core.model_mixins import StrFromFieldsMixin
from petstagram_last.pets.models import Pet
from petstagram_last.photos.validators import validate_file_less_than_5mb

UserModel= get_user_model()
# Create your models here.
class Photo(StrFromFieldsMixin, models.Model):
    MIN_LENGTH_DESCRIPTION=10
    MAX_LENGTH_DESCRIPTION = 300
    MAX_LENGTH_LOCATION=30
    str_fields=('photo',)
    photo=models.ImageField(
        validators=(
            validate_file_less_than_5mb,
        ),
        upload_to='photos',
        null=False,
        blank=False,

    )

    description= models.CharField(
        max_length=MAX_LENGTH_DESCRIPTION,
        validators=(
            MinLengthValidator(MIN_LENGTH_DESCRIPTION, message=f'Минималната дължина на описанието е {MIN_LENGTH_DESCRIPTION}'),
        ),
        null=True,
        blank=True,
    )

    location=models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )

    date_of_publication=models.DateField(
        auto_now= True,
        null=False,
        blank=True,
    )

    tagged_pets=models.ManyToManyField(
        Pet,
        blank=True,
    )
    user=models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )