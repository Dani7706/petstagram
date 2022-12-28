from django import forms

from petstagram_last.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('text',)
        widgets={
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                }
            )
        }

class SearchForm(forms.Form):
    pet_name= forms.CharField(
        max_length=50,
        required=False,
    )