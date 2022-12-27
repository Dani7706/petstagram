from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram_last.core.model_mixins import StrFromFieldsMixin

UserModel= get_user_model()
# Create your models here.
class Pet(StrFromFieldsMixin, models.Model):
    MAX_LENGTH_NAME = 30
    str_fields = ('name',)
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    user= models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super(Pet, self).save(*args, **kwargs)
