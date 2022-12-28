from django.contrib.auth import get_user_model
from django.db import models

from petstagram_last.photos.models import Photo


UserModel=get_user_model()

class Comment(models.Model):
    MAX_LENGTH_TEXT=300
    text=models.CharField(
        max_length=MAX_LENGTH_TEXT,
        null=False,
        blank=False
    )
    date_time_of_publication=models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )
    photo= models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user=models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

class Like(models.Model):
    photo= models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user= models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )