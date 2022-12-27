from django import forms

from petstagram_last.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model=Pet
        fields=('name', 'date_of_birth', 'personal_photo')
        widgets={
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            )
        }
        labels={
            'name': 'Pet Name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image'
        }

class PetCreateForm(PetBaseForm):
    pass

class PetEditForm(PetBaseForm):
    pass

class PetDeleteForm(PetBaseForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for (_, field) in self.fields.items():
            # field.widget.attrs['disabled']= 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

