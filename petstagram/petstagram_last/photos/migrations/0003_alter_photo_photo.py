# Generated by Django 4.1.3 on 2022-11-29 10:38

from django.db import migrations, models
import petstagram_last.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_create_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles/photos', validators=[petstagram_last.photos.validators.validate_file_less_than_5mb]),
        ),
    ]