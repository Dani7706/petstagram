from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram_last.accounts.forms import RegisterForm
from petstagram_last.accounts.models import Gender

UserModel= get_user_model()

class Register(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response= super().post(request,*args,**kwargs)
        login(request, self.object)
        return response


class LogIn(LoginView):
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')

class LogOut(LogoutView):
    next_page = reverse_lazy('index')



class ProfileDetails(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):

        context= super(ProfileDetails, self).get_context_data()
        gender=""
        if self.object.gender:
            gender=[value for key,value in Gender.choices() if key== self.object.gender and self.object.gender is not None][0]
        photos = self.object.photo_set.prefetch_related('like_set')
        context['full_name']=self.object.get_full_name()
        context['is_owner']= self.object==self.request.user
        context['photos_count']=photos.count()
        context['likes_count']=sum(x.like_set.count() for x in photos)
        context['pets_count']=self.object.pet_set.count()
        context['gender']=gender
        context['photos']=self.object.photo_set.all()
        context['pets']=self.object.pet_set.all()
        return context



class ProfileEdit(UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'
    fields = ('first_name','last_name','username','email','gender')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk':self.object.pk,
        })



class ProfileDelete(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')