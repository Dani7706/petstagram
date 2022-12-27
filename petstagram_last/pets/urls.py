from django.urls import path, include

from petstagram_last.pets.views import pet_delete, PetAddView, pet_details, pet_edit

urlpatterns=(
    path('add/', PetAddView.as_view(), name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details, name= 'pet details'),
        path('edit/', pet_edit, name='pet edit'),
        path('delete/', pet_delete, name='pet delete'),
    ]))
)