from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram_last.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram_last.photos.models import Photo




#
# def photo_details(request, pk):
#     photo= Photo.objects.get(id=pk)
#     likes=photo.like_set.all()
#     comments=photo.comment_set.all()
#     context={
#         'photo':photo,
#         'likes':likes,
#         'comments':comments,
#     }
#     return render(request, 'photos/photo-details-page.html', context=context)

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context= super(PhotoDetailsView, self).get_context_data()
        photo=Photo.objects.filter(pk=self.object.pk).get()
        context['photo']=photo
        context['likes']=photo.like_set.all()
        context['comments']=photo.comment_set.all()
        context['user']=self.object.user
        return context

# def photo_add(request):
#     if request.method=="GET":
#         form= PhotoCreateForm()
#     else:
#         form= PhotoCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context={
#         'form': form
#     }
#     return render(request, 'photos/photo-add-page.html', context)
class PhotoAddView(CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    fields = ("photo",'description','location','tagged_pets')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(PhotoAddView, self).form_valid(form)

# def photo_edit(request, pk):
#     photo=Photo.objects.filter(pk=pk).get()
#     if request.method=="GET":
#         form = PhotoEditForm(instance=photo)
#     else:
#         form= PhotoEditForm(request.POST, request.FILES, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photo details' , pk=photo.pk)
#
#     context={
#         'form': form,
#         'pk': pk,
#     }
#     return render(request, 'photos/photo-edit-page.html', context)

class PhotoEditView(UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse_lazy('photo details', kwargs={
            'pk': self.object.pk
        })
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(PhotoEditView, self).form_valid(form)



def photo_delete(request, pk):
    photo= Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('index')