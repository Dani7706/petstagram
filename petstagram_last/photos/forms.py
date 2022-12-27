from django import forms

from petstagram_last.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('photo', 'description', 'location','tagged_pets')
        labels={
            'photo': 'Photo file',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag Pets'
        }

class PhotoCreateForm(PhotoBaseForm):
    pass

class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model=Photo
        exclude=('photo',)


class PhotoDeleteForm(PhotoBaseForm):
    pass