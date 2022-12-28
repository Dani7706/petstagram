from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram_last.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram_last.pets.models import Pet
from petstagram_last.pets.utils import get_pet_by_slug_and_username





def pet_details(request, username,pet_slug):
    pet=get_pet_by_slug_and_username(pet_slug, username)
    pet_photos=pet.photo_set.all()
    photos_count= pet_photos.count()
    context={
        'pet': pet,
        'pet_photos': pet_photos,
        'photos_count':photos_count,
    }
    return render(request, 'pets/pet-details-page.html', context,)

# class PetDetailsView(DetailView):
#     model = Pet
#     template_name = 'pets/pet-details-page.html'
#
#     def get_context_data(self, **kwargs):
#         context=super(PetDetailsView, self).get_context_data()
#         pet = get_pet_by_slug_and_username(self.object.slug, self.request.user.username)
#         pet_photos = pet.photo_set.all()
#         photos_count = pet_photos.count()
#         context['pet']=pet
#         context['pet_photos']=pet_photos
#         context['photos_count']=photos_count
#         return context

# def pet_add(request):
#     if request.method =='GET':
#         form = PetCreateForm()
#     else:
#         form = PetCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details', pk=1)
#
#     context={
#         'form': form
#     }
#     return render(request, 'pets/pet-add-page.html', context)

class PetAddView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    # fields = ('name','date_of_birth','personal_photo',)
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super(PetAddView, self).form_valid(form)

def pet_edit(request, username,pet_slug):
    pet= get_pet_by_slug_and_username(pet_slug, username)
    if request.method =='GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            pet=form.save(commit=False)
            pet.user=request.user
            pet.save()

            return redirect('pet details', username, pet_slug)

    context={
        'form': form,
        'pet_slug':pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)

# class PetEditView(UpdateView):
#     model = Pet
#     form_class = PetEditForm
#     template_name = 'pets/pet-edit-page.html'
#
#
#     def get_success_url(self):
#
#         return reverse_lazy('pet details', kwargs={
#             'username': self.request.user,
#             'slug': self.object.slug,
#         })
#
#     def form_valid(self, form):
#
#         form.instance.user=self.request.user
#         return super(PetEditView, self).form_valid(form)

def pet_delete(request, username,pet_slug):
    pet = get_pet_by_slug_and_username(pet_slug,username)
    if request.method=='GET':
        form = PetDeleteForm(instance=pet)
    else:
        form= PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()
            return redirect('profile details', pk=pet.user.pk)

    context={
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)
