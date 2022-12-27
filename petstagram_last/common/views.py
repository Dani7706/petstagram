from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_last.common.forms import CommentForm, SearchForm
from petstagram_last.common.models import Like
from petstagram_last.photos.models import Photo


def index(request):
    search_form= SearchForm(request.GET)
    search_pattern=None
    if search_form.is_valid():
        search_pattern=search_form.cleaned_data['pet_name']
    photos=Photo.objects.all()
    if search_pattern:
        photos=photos.filter(tagged_pets__name__icontains=search_pattern)
    context={
        'photos': photos,
        'comment_form': CommentForm(),
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context=context)

@login_required
def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object= Like.objects.filter(photo_id=photo.id, user=request.user)

    if not liked_object and photo.user != request.user:

        like=Like(photo=photo)
        like.user= request.user
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

@login_required
def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

@login_required
def comment_photo(request, photo_id):
    photo= Photo.objects.filter(pk=photo_id).get()
    form = CommentForm(request.POST)
    if form.is_valid():
        comment= form.save(commit=False)
        comment.photo=photo
        comment.user= request.user
        comment.save()

    return redirect('index')